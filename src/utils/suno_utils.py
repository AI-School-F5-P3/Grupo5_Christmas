import requests

def generate_carol(description, details, music_type):
    api_url = "https://api.suno.com/generate_carol"
    payload = {
        "description": description,
        "details": details,
        "music_type": music_type
    }
    response = requests.post(api_url, json=payload)
    return response.json().get("carol", "Error generating carol")