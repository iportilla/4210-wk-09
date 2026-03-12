import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)

def get_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

def run_prompt(prompt: str) -> str:
    client = get_client()
    response = client.responses.create(
        model=get_model(),
        input=prompt,
    )
    return response.output_text
