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
        # First check if we already have a cached image
        cached_image = cache.get('daily_image_url')
        if cached_image:
            return cached_image
            
        # Set a shorter timeout for the API call
        api_key = os.getenv('OPENAI_API_KEY')
        client = OpenAI(api_key=api_key, timeout=25.0)  # 25 second timeout
        
        prompt = f"Create a photorealistic image inspired by the following words: {quote}. The scene should be inspiring and visually pleasing. Focus on realism with rich details. The image should be visually balanced and optimized for display on both mobile and desktop screens."
        
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        cache.set('daily_image_url', image_url)
        return image_url
        
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        # Return a default image URL if generation fails
        return "https://via.placeholder.com/1024x1024.png?text=Daily+Inspiration"

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

def get_initial_image_url():
    """Get a cached image or return default"""
    cached_image = cache.get('daily_image_url')
    return cached_image if cached_image else "https://via.placeholder.com/1024x1024.png?text=Loading+Daily+Image"

def refresh_all_data():
    """Refresh all cached data except image"""
    try:
        eastern = pytz.timezone('America/New_York')
        current_time = datetime.now(eastern)
        
        # Get and cache the date
        current_date = current_time.strftime('%B %d, %Y')
        cache.set('current_date', current_date)
        
        # Get and cache quote
        quote_data = get_daily_quote()
        cache.set('quote_data', quote_data)
        
        # Get and cache tips
        daily_tips = get_daily_tips()
        cache.set('daily_tips', daily_tips)
        
        # Get and cache podcasts
        podcasts = get_all_spotify_podcasts()
        cache.set('podcasts', podcasts)
        
        # Store refresh time
        cache.set('last_refresh_time', current_time)
        
        # Start background image generation
        try:
            daily_image_url = get_daily_image_url(quote_data['quote'])
            cache.set('daily_image_url', daily_image_url)
        except Exception as e:
            print(f"Error during image generation: {str(e)}")
            # Keep existing image or use default
            if not cache.get('daily_image_url'):
                cache.set('daily_image_url', "https://via.placeholder.com/1024x1024.png?text=Daily+Inspiration")
        
        return current_date, podcasts, get_initial_image_url(), daily_tips, quote_data
        
    except Exception as e:
        print(f"Error in refresh_all_data: {str(e)}")
        return (
            datetime.now(eastern).strftime('%B %d, %Y'),
            [],
            "https://via.placeholder.com/1024x1024.png?text=Daily+Inspiration",
            {'parenting': 'Tip unavailable', 'nutrition': 'Tip unavailable'},
            {'quote': 'Quote unavailable', 'author': '', 'year': ''}
        )

@app.before_request
def check_cache():
    """Check if cache needs refresh before each request"""
    if should_refresh_cache():
        refresh_all_data()

@app.route('/')
def home():
    current_date = cache.get('current_date')
    quote_data = cache.get('quote_data')
    daily_image_url = get_initial_image_url()
    
    if current_date is None or quote_data is None:
        current_date, _, daily_image_url, _, quote_data = refresh_all_data()
        
    return render_template('daily_quote_and_image.html', 
                         daily_image_url=daily_image_url,
                         quote=quote_data['quote'],
                         author=quote_data['author'],
                         year=quote_data['year'])

@app.route('/tips')
def tips():
    current_date = cache.get('current_date')
    daily_tips = cache.get('daily_tips')
    
    if current_date is None or daily_tips is None:
        current_date, _, _, daily_tips, _ = refresh_all_data()
        
    return render_template('tips.html', 
                         current_date=current_date,
                         parenting_tip=daily_tips['parenting'],
                         nutrition_tip=daily_tips['nutrition'])

@app.route('/podcasts')
def podcasts():
    podcast_data = cache.get('podcasts')
    if podcast_data is None:
        _, podcast_data, _, _ = refresh_all_data()
    return render_template('podcasts.html', 
                         top_podcasts=podcast_data['top_podcasts'],
                         top_episodes=podcast_data['top_episodes'],
                         health_fitness=podcast_data['health_fitness'])

@app.route('/about')
def about():
    current_date = cache.get('current_date')
    if current_date is None:
        current_date, _, _, _ = refresh_all_data()
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

# Add a route to check/update image status
@app.route('/check_image')
def check_image():
    image_url = cache.get('daily_image_url')
    return jsonify({'image_url': image_url if image_url else get_initial_image_url()})

if __name__ == '__main__':
    # Initial cache population
    refresh_all_data()
    app.run(debug=True) 