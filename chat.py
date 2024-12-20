import os
from openai import OpenAI

class ChatBot:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.client = OpenAI(api_key=api_key)
        self.conversation_history = []
        self.follow_up_used = False
        self.tips_clicked = set()

    def get_parenting_prompt(self, tip):
        return (f"Take the role of an expert in parenting and relationship advice. "
                f"Tell me more about the quote '{tip}', expand about what it means and its broader "
                f"context related to relationships with children, family, and spouse, and talk about "
                f"what evidence there is, if any, to support this advice. Be thorough and detailed with this initial response."
                f"However, unless told otherwise, subsequent questions, comments, or queries can be answered directly and need "
                f"not reference or pertain to the original quote.")

    def get_nutrition_prompt(self, tip):
        return (f"Take the role of an expert in nutrition, health, and longevity. "
                f"Tell me more about the quote '{tip}', expand about what it means and its broader "
                f"context related to health, well-being, fitness, and longevity, and what evidence "
                f"there is, if any, to support this advice. Be thorough and detailed with this initial response."
                f"However, unless told otherwise, subsequent questions, comments, or queries can be answered directly and need "
                f"not reference or pertain to the original quote.")
            

    def get_follow_up_prompt(self, question):
        return f"Answer this question directly and concisely: {question}"

    def get_response(self, message, tip, chat_type):
        try:
            # Check if this tip has already been clicked
            tip_id = f"{chat_type}:{tip}"
            is_new_tip = tip_id not in self.tips_clicked

            # If it's a new tip click
            if is_new_tip and tip:  # Only process as new tip if tip is provided
                self.tips_clicked.add(tip_id)
                prompt = self.get_parenting_prompt(tip) if chat_type == "parenting" else self.get_nutrition_prompt(tip)
                messages = [{"role": "user", "content": prompt}]
                model = "gpt-4o-mini"
                temp = 0.9
                max_tokens = 500
                footer = "\n\nIf you havn't already, please select another tip or ask a question. Otherwise, check back tomorrow for another set of tips!"
            
            # If it's a follow-up question
            elif message and not self.follow_up_used:
                messages = [
                    {"role": "system", "content": "You are a helpful assistant. Answer questions directly in 1-2 sentences. Do not mention or assume any context about nutrition, parenting, or previous conversations."},
                    {"role": "user", "content": message}  # Use raw message instead of prompt
                ]
                model = "gpt-4o-mini"
                temp = 0.7
                max_tokens = 200
                self.follow_up_used = True
                footer = "\n\nPlease select the other tip if you havn't already or check back tomorrow for another set of tips!"
            
            # If user tries to ask more questions
            elif self.follow_up_used:
                return "I'm sorry, but I cannot respond to any more comments or questions today. Please try again tomorrow."

            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temp
            )

            response_text = response.choices[0].message.content
            
            # Only store conversation history for initial tips
            if is_new_tip:
                self.conversation_history = messages + [{"role": "assistant", "content": response_text}]

            # Format response
            lines = response_text.split('\n')
            formatted_lines = []
            
            for line in lines:
                if line.strip() and line[0].isdigit() and line.strip()[1:].startswith('.'):
                    formatted_lines.append('')
                    formatted_lines.append(line.strip())
                else:
                    formatted_lines.append(line)
            
            response_text = '\n'.join(formatted_lines)
            return response_text + footer

        except Exception as e:
            return f"I apologize, but I encountered an error: {str(e)}"
