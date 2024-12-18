from flask import Flask, render_template, jsonify, request
from datetime import datetime
from scraping import get_all_spotify_podcasts
from quotes_db import get_random_quote
from tips_db import get_random_tip
from dotenv import load_dotenv
import os
from openai import OpenAI
from dotenv import load_dotenv
from chat import ChatBot

app = Flask(__name__)

def get_daily_image_url(quote):
    try:
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            raise ValueError("OpenAI API key not found in environment variables")
            
        client = OpenAI(api_key=api_key)
        prompt = f"Create a photorealistic image inspired by the following words: {quote}. The scene should be inspiring and visually pleasing. Focus on realism with rich details. The image should be visually balanced and optimized for display on both mobile and desktop screens."
        print(prompt)
        
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        return image_url
        
    except Exception as e:
        return "https://via.placeholder.com/1024x1024.png?text=Image+Generation+Failed"

@app.context_processor
def inject_current_date():
    # This makes current_date available in all templates.
    current_date = datetime.now().strftime("%B %d, %Y")
    return dict(current_date=current_date)

@app.route('/')
def daily_quote_and_image():
    # First get the quote
    quote_data = get_random_quote()
    
    daily_image_url = get_daily_image_url(quote_data['quote'])
    # daily_image_url = "https://via.placeholder.com/1024x1024.png?text=Image+Generation+Disabled"
    
    return render_template('daily_quote_and_image.html', 
                         daily_image_url=daily_image_url, 
                         quote=quote_data['quote'],
                         author=quote_data['author'],
                         year=quote_data['year'])

@app.route('/tips')
def tips():
    parenting_tip = get_random_tip('parenting')
    nutrition_tip = get_random_tip('nutrition')
    return render_template('tips.html', tip1=parenting_tip, tip2=nutrition_tip)

@app.route('/podcasts')
def podcasts():
    # Get all podcast data
    try:
        all_podcasts = get_all_spotify_podcasts()
        return render_template('podcasts.html', 
                             top_podcasts=all_podcasts['top_podcasts'],
                             top_episodes=all_podcasts['top_episodes'],
                             health_fitness=all_podcasts['health_fitness'])
    except Exception as e:
        print(f"Error fetching podcasts: {e}")
        # Return empty lists if there's an error
        return render_template('podcasts.html', 
                             top_podcasts=[],
                             top_episodes=[],
                             health_fitness=[])

@app.route('/about')
def about():
    linkedin_url = "https://www.linkedin.com/in/joaquin-de-rojas-598830268/"
    X_url = "https://x.com/JdeRojasMD"
    return render_template('about.html', linkedin_url=linkedin_url, X_url=X_url)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    tip = data.get('tip')
    chat_type = data.get('type')
    
    response = chatbot.get_response(message, tip, chat_type)
    return jsonify({'response': response})

chatbot = ChatBot()

if __name__ == '__main__':
    app.run(debug=True) 