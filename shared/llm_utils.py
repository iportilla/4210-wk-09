import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file in project root
load_dotenv()

# Default system prompt for all exercises
DEFAULT_SYSTEM = "You are a helpful assistant that explains complex topics clearly and concisely."

def get_client() -> OpenAI:
    """
    Create and return an authenticated OpenAI client.
    Raises ValueError if OPENAI_API_KEY is not set.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)


def get_model() -> str:
    """
    Return the model name to use for API calls.
    Defaults to 'gpt-4.1-mini' if OPENAI_MODEL env var is not set.
    """
    return os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def run_prompt(prompt: str) -> str:
    """
    Send a prompt to the OpenAI API and return the response text.
    
    Args:
        prompt: The text prompt to send to the model
        
    Returns:
        The model's response as a string
    """
    client = get_client()
    response = client.responses.create(
        model=get_model(),
        input=prompt,
    )
    return response.output_text


def st_run_prompt(prompt: str, system: str = None) -> str:
    """
    Send a prompt to OpenAI's chat API with optional system prompt.
    
    Args:
        prompt: The user's message/question to send
        system: Optional system prompt to set AI behavior/persona
        
    Returns:
        The model's response as a string
    """
    # Get authenticated OpenAI client
    client = get_client()
    
    # Build messages list in OpenAI chat format
    messages = []
    
    # Add system message first if provided (sets AI's behavior)
    if system:
        messages.append({"role": "system", "content": system})
    
    # Add the user's prompt
    messages.append({"role": "user", "content": prompt})
    
    # Call OpenAI chat completions API
    response = client.chat.completions.create(
        model=get_model(),
        messages=messages,
    )
    
    # Extract and return the text from the first response choice
    return response.choices[0].message.content