# WifeApp2

A personalized Flaskweb application providing daily inspiration, tips, and resources for a balanced life. Features daily quotes with AI-generated images, parenting and nutrition tips with expert chat functionality, and curated podcast recommendations.

## Features

- **Daily Quote & AI Image**: Each day features an inspiring quote paired with a DALL-E generated image that visually represents the quote's message
- **Daily Tips**: 
  - Parenting advice for growing families
  - Nutrition guidance for healthy living
- **Podcast Recommendations**: 
  - Top trending podcasts
  - Featured health & fitness episodes
  - Popular episode highlights
- **Interactive Chat**: AI-powered chat system for discussing the daily tips and getting personalized advice
- **Automatic Daily Refresh**: Content automatically updates daily at midnight EST

## Technical Stack

- **Backend**: Python/Flask
- **AI Integration**: OpenAI API (DALL-E 2 for images, GPT for chat)
- **Caching**: Redis for persistent data storage
- **Frontend**: HTML/CSS/JavaScript
- **Deployment**: Heroku

## Environment Variables

Required environment variables:

```
OPENAI_API_KEY=your_openai_api_key
REDISCLOUD_URL=your_redis_cloud_url
FLASK_ENV=development/production
```

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
cd wifeapp2
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```



## Running Locally

1. Start the Flask server:
```bash
python app.py
```

2. Visit `http://localhost:5000` in your browser

## Deployment

### Prerequisites
- Python 3.10+
- Git
- OpenAI API key

### Server Deployment Steps
1. Set up your server environment
2. Clone the repository
3. Install dependencies
4. Set up environment variables
5. Configure your web server (e.g., Nginx/Apache)
6. Set up SSL certificate
7. Start the application

## Update Schedule
- Quotes & Images: Daily updates
- Tips: Daily updates
- Podcasts: Daily updates

## Contributing
This is a personal project, but suggestions and improvements are welcome.

## License
Private - All Rights Reserved

## Author
Joaquin de Rojas
