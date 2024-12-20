from flask import Flask, render_template, jsonify, request
from datetime import datetime, date
from scraping import get_all_spotify_podcasts
from quotes import get_daily_quote
from tips import get_daily_tips
import os
from openai import OpenAI
from chat import ChatBot
import pytz

app = Flask(__name__)

# No need for dotenv in production
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Only load dotenv in development
if os.environ.get('FLASK_ENV') != 'production':
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

def get_daily_image_url(quote):
    try:
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
def home():
    # Get current UTC time from datetime
    utc_now = datetime.now(pytz.UTC)
    
    # Convert to US Eastern Time
    eastern = pytz.timezone('America/New_York')
    eastern_time = utc_now.astimezone(eastern)
    
    # Format the date
    current_date = eastern_time.strftime('%B %d, %Y')
    
    return render_template('index.html', current_date=current_date)

@app.route('/tips')
def tips():
    daily_tips = get_daily_tips()
    return render_template('tips.html', 
                         parenting_tip=daily_tips['parenting'],
                         nutrition_tip=daily_tips['nutrition'])

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