# Career Guidance Chatbot

An interactive career guidance chatbot powered by Groq AI that helps users explore career paths, get professional advice, and make informed decisions about their careers.

## Features

- 🤖 AI-powered career guidance
- 💬 Real-time chat interface
- 🎯 Personalized career recommendations
- 📱 Responsive design
- ⚡ Fast and intuitive UI

## Live Demo

[Add your deployed application URL here]

## Technologies Used

- Python 3.9+
- Flask
- Groq AI API
- HTML/CSS/JavaScript
- Tailwind CSS
- Gunicorn (Production server)

## Prerequisites

- Python 3.9 or higher
- Groq API key
- Git

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/career-guidance-chatbot.git
cd career-guidance-chatbot
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add:
```
GROQ_API_KEY=your_api_key_here
```

5. Run the application:
```bash
python app.py
```

6. Open http://localhost:5000 in your browser

## Deployment

### Deploying to Heroku

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Set environment variables:
```bash
heroku config:set GROQ_API_KEY=your_api_key_here
```

4. Deploy the application:
```bash
git push heroku main
```

### Alternative Deployment Options

- **Railway**: Deploy directly from GitHub repository
- **Render**: Use the Render dashboard to deploy from GitHub

## API Reference

The chatbot uses the Groq AI API for natural language processing. Endpoints:

- `GET /`: Serves the chat interface
- `POST /chat`: Processes user messages and returns AI responses

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 