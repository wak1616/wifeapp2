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
import redis  # for persistent caching (that persists between dyno restarts; SimpleCache just stores everything in memory)
from threading import Thread


app = Flask(__name__)

# Update to use REDISCLOUD_URL
redis_url = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379/0')
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_URL'] = redis_url
app.config['CACHE_DEFAULT_TIMEOUT'] = 86400  # 24 hours

cache = Cache(app)

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
    """Makes current_date available in all templates using the same format and timezone as refresh_all_data"""
    eastern = pytz.timezone('America/New_York')
    current_date = datetime.now(eastern).strftime('%B %d, %Y')
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

def generate_image_async(quote):
    """Generate image in background and cache it"""
    try:
        daily_image_url = get_daily_image_url(quote)
        if daily_image_url and 'placeholder.com' not in daily_image_url:
            cache.set('daily_image_url', daily_image_url, timeout=86400)
    except Exception as e:
        print(f"Error in async image generation: {str(e)}")

def refresh_all_data():
    """Refresh all cached data"""
    try:
        eastern = pytz.timezone('America/New_York')
        current_time = datetime.now(eastern)
        
        # Get and cache quote first
        quote_data = get_daily_quote()
        cache.set('quote_data', quote_data, timeout=86400)
        
        # Start image generation in background
        Thread(target=generate_image_async, args=(quote_data['quote'],)).start()
        
        # Cache other data
        current_date = current_time.strftime('%B %d, %Y')
        cache.set('current_date', current_date, timeout=86400)
        daily_tips = get_daily_tips()
        cache.set('daily_tips', daily_tips, timeout=86400)
        
        # Get and cache podcasts
        podcasts = get_all_spotify_podcasts()
        cache.set('podcasts', podcasts, timeout=86400)
        
        cache.set('last_refresh_time', current_time, timeout=86400)
        
        return current_date, podcasts, daily_tips, quote_data
        
    except Exception as e:
        print(f"Error in refresh_all_data: {str(e)}")
        return (
            datetime.now(eastern).strftime('%B %d, %Y'),
            [],
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
    daily_image_url = cache.get('daily_image_url')
    
    if quote_data is None:
        _, _, _, quote_data = refresh_all_data()
    
    # Use cached image or placeholder
    if not daily_image_url:
        daily_image_url = "https://via.placeholder.com/1024x1024.png?text=Loading+Daily+Image"
    
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

@app.route('/generate_image')
def generate_image():
    """Endpoint to generate and cache the daily image"""
    try:
        print("Starting image generation process...")
        quote_data = cache.get('quote_data')
        
        if not quote_data:
            print("No quote data found in cache")
            return jsonify({'image_url': "https://via.placeholder.com/1024x1024.png?text=Quote+Not+Found"})
        
        print(f"Generating image for quote: {quote_data['quote'][:50]}...")
        daily_image_url = get_daily_image_url(quote_data['quote'])
        
        if daily_image_url and 'placeholder.com' not in daily_image_url:
            print(f"Successfully generated image: {daily_image_url[:50]}...")
            cache.set('daily_image_url', daily_image_url)
            return jsonify({'image_url': daily_image_url})
        else:
            print("Image generation returned placeholder or None")
            return jsonify({'image_url': "https://via.placeholder.com/1024x1024.png?text=Generation+Failed"})
            
    except Exception as e:
        print(f"Error in generate_image: {str(e)}")
        return jsonify({'image_url': "https://via.placeholder.com/1024x1024.png?text=Error+Occurred"})

@app.route('/check_image')
def check_image():
    """Check if image is ready"""
    try:
        print("Checking image status...")
        image_url = cache.get('daily_image_url')
        print(f"Current cached image URL: {image_url[:50] if image_url else 'None'}")
        
        if image_url and 'placeholder.com' not in image_url:
            return jsonify({'image_url': image_url})
        return jsonify({'image_url': "https://via.placeholder.com/1024x1024.png?text=Loading+Daily+Image"})
    except Exception as e:
        print(f"Error checking image: {str(e)}")
        return jsonify({'image_url': "https://via.placeholder.com/1024x1024.png?text=Error+Checking"})

if __name__ == '__main__':
    # Initial cache population
    refresh_all_data()
    app.run(debug=True) 