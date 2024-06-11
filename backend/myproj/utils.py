import requests
from django.conf import settings 

def get_gemini_response(prompt):
    url = "http://127.0.0.1:8000/chat"  # Example endpoint, replace with the correct one
    headers = {
        'Authorization': f'Bearer {settings.GEMINI_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'prompt': prompt,
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
