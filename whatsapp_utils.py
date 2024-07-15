import os
import requests


def update_whatsapp_status(media_url, caption):
    api_url = os.getenv('WHAPI_API_URL')
    token = os.getenv('WHAPI_TOKEN')
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }
    payload = {
        "media": media_url,
        "contacts": ['62895704806187'],  # Example contact, replace with actual
        "caption": caption,
        "width": 770,
        "height": 770
    }
    response = requests.post(f'{api_url}stories', json=payload, headers=headers)
    return response.status_code == 200
