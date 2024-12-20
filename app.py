from flask import Flask, render_template, jsonify, request
from datetime import datetime, date
from scraping import get_all_spotify_podcasts
from quotes import get_daily_quote
from tips import get_daily_tips
import os
from openai import OpenAI
from chat import ChatBot
import pytz
from flask_caching import Cache

app = Flask(__name__)

# Configure Flask-Caching
cache = Cache(app, config={
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 0  # No timeout, we'll manually invalidate
})

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

def should_refresh_cache():
    """Check if we need to refresh the cache (true if last refresh was before today's midnight EST)"""
    eastern = pytz.timezone('America/New_York')
    now = datetime.now(eastern)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    last_refresh = cache.get('last_refresh_time')
    return last_refresh is None or last_refresh < midnight

def refresh_all_data():
    """Refresh all cached data"""
    eastern = pytz.timezone('America/New_York')
    current_time = datetime.now(eastern)
    
    # Get and cache the date
    current_date = current_time.strftime('%B %d, %Y')
    cache.set('current_date', current_date)
    
    # Get and cache podcasts
    podcasts = get_all_spotify_podcasts()
    cache.set('podcasts', podcasts)
    
    # Store refresh time
    cache.set('last_refresh_time', current_time)
    
    return current_date, podcasts

@app.before_request
def check_cache():
    """Check if cache needs refresh before each request"""
    if should_refresh_cache():
        refresh_all_data()

@app.route('/')
def home():
    current_date = cache.get('current_date')
    if current_date is None:
        current_date, _ = refresh_all_data()
    return render_template('daily_quote_and_image.html', 
                         daily_image_url=daily_image_url, 
                         quote=quote_data['quote'],
                         author=quote_data['author'],
                         year=quote_data['year'])

@app.route('/tips')
def tips():
    current_date = cache.get('current_date')
    if current_date is None:
        current_date, _ = refresh_all_data()
    return render_template('tips.html', 
                         parenting_tip=daily_tips['parenting'],
                         nutrition_tip=daily_tips['nutrition'])

@app.route('/podcasts')
def podcasts():
    podcast_data = cache.get('podcasts')
    if podcast_data is None:
        _, podcast_data = refresh_all_data()
    return render_template('podcasts.html', 
                         top_podcasts=podcast_data['top_podcasts'],
                         top_episodes=podcast_data['top_episodes'],
                         health_fitness=podcast_data['health_fitness'])

@app.route('/about')
def about():
    current_date = cache.get('current_date')
    if current_date is None:
        current_date, _ = refresh_all_data()
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
    # Initial cache population
    refresh_all_data()
    app.run(debug=True) 