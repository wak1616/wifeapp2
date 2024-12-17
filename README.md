# WifeApp2

A personalized web application providing daily inspiration, tips, and resources for a balanced life. Features daily quotes with AI-generated images, parenting and nutrition tips with expert chat functionality, and curated podcast recommendations.

## Features

- 🎯 Daily inspirational quotes with AI-generated images
- 💭 Interactive expert chat for parenting and nutrition advice
- 🎧 Weekly updated podcast recommendations
- 📱 Responsive design for all devices

## Tech Stack

- Backend: Python/Flask
- Frontend: HTML, CSS, JavaScript
- Database: SQLite
- AI Integration: OpenAI (GPT-4, DALL-E)
- External APIs: Spotify Web Scraping

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

4. Create `.env` file with required environment variables:
```
OPENAI_API_KEY=your_openai_api_key
```

5. Initialize the databases:
```bash
./reset_dbs.sh
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
- Podcasts: Weekly updates

## Environment Variables
Create a `.env` file with the following:
```
OPENAI_API_KEY=your_openai_api_key
```

## Contributing
This is a personal project, but suggestions and improvements are welcome.

## License
Private - All Rights Reserved

## Author
Joaquin de Rojas
