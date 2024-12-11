import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("DALLE_ENDPOINT")
openai.api_version = "2024-02-01"

def generate_image(prompt):
    response = openai.Image.create(
        engine="dall-e-3",
        prompt=prompt
    )
    return response['data'][0]['url']