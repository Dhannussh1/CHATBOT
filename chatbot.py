import requests
import logging
from .utils import load_api_key

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'
MODEL = "llama3-70b-8192"
GROQ_API_KEY = load_api_key()

def chat_with_groq(user_input):
    """
    Send a message to Groq API and get the response
    
    Args:
        user_input (str): User's message
        
    Returns:
        str: Chatbot's response
    """
    try:
        if not user_input.strip():
            return "I didn't receive any message. Could you please try again?"

        headers = {
            'Authorization': f'Bearer {GROQ_API_KEY}',
            'Content-Type': 'application/json',
        }

        messages = [
            {"role": "system", "content": (
                "You are a professional career guidance counselor. "
                "Your goal is to help the user figure out career paths based on their skills, interests, and doubts. "
                "Give detailed, practical, and encouraging advice. "
                "If they mention their skills, recommend careers or courses. "
                "If they seem confused, ask guiding questions to help them clarify."
            )},
            {"role": "user", "content": user_input},
        ]

        payload = {
            "model": MODEL,
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 1024,
            "stream": False
        }

        logger.info(f"Sending request to Groq API for input: {user_input[:50]}...")
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        if not result.get('choices'):
            raise ValueError("No choices in response")
            
        return result['choices'][0]['message']['content'].strip()
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API Request Error: {str(e)}")
        return "I apologize, but I'm having trouble connecting to the server. Please try again later."
    
    except (KeyError, IndexError, ValueError) as e:
        logger.error(f"Response Parsing Error: {str(e)}")
        return "I apologize, but I received an unexpected response. Please try again."
    
    except Exception as e:
        logger.error(f"Unexpected Error: {str(e)}")
        return "I apologize, but something went wrong. Please try again later."

if __name__ == "__main__":
    print("Career Guidance Chatbot (type 'exit' to quit)")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! Wishing you the best in your career journey!")
                break
            response = chat_with_groq(user_input)
            print(f"Chatbot: {response}")
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye! Have a great day!")
            break
        except Exception as e:
            logger.error(f"Main loop error: {str(e)}")
            print("An error occurred. Please try again.") 