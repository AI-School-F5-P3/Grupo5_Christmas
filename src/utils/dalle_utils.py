import openai

openai.api_key = "your_openai_api_key"

def generate_postcard(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']