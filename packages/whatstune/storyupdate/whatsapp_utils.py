import os
import requests

from file_utils import read_contacts


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
        "contacts": read_contacts(),
        "caption": caption,
        "width": 770,
        "height": 770
    }
    response = requests.post(f'{api_url}stories', json=payload, headers=headers)
    return response.status_code == 200
