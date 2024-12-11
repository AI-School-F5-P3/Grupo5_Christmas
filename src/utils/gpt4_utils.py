import openai

openai.api_key = "your_openai_api_key"

def generate_recipes(prompt):
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=f"Generate a menu based on the following characteristics: {prompt}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def generate_email_text(prompt):
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=f"Generate an email text for a Christmas postcard based on the following prompt: {prompt}",
        max_tokens=150
    )
    return response.choices[0].text.strip()