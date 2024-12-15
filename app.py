from flask import Flask, render_template
from datetime import datetime
from scraping import get_all_spotify_podcasts
from quotes_db import get_random_quote

app = Flask(__name__)

def get_daily_image_url():
    return "https://picsum.photos/1200/600?random=1"

@app.context_processor
def inject_current_date():
    # This makes current_date available in all templates.
    current_date = datetime.now().strftime("%B %d, %Y")
    return dict(current_date=current_date)

@app.route('/')
def daily_quote_and_image():
    daily_image_url = get_daily_image_url()
    quote_data = get_random_quote()
    return render_template('daily_quote_and_image.html', 
                         daily_image_url=daily_image_url, 
                         quote=quote_data['quote'],
                         author=quote_data['author'],
                         year=quote_data['year'])

@app.route('/tips')
def tips():
    parenting_tip = "Encourage open communication; listen actively to your children without immediate judgment."
    nutrition_tip = "Incorporate more whole foods into your diet; aim for colorful fruits and vegetables daily."
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
    description = "WifeApp (ver2) is dedicated to providing daily inspiration and tips for a balanced life."
    return render_template('about.html', description=description)

if __name__ == '__main__':
    app.run(debug=True) 