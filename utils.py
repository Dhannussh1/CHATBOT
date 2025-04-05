import os
from dotenv import load_dotenv

def load_api_key():
    """Load and validate API key from environment variables"""
    load_dotenv()
    api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY environment variable is not set. "
            "Please set it in your .env file or environment variables."
        )
    
    return api_key

def get_port():
    """Get port from environment variables with fallback"""
    return int(os.environ.get('PORT', 5000))

def is_development():
    """Check if running in development mode"""
    return os.environ.get('FLASK_ENV') == 'development' 