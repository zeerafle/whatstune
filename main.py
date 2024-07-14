import pylast
from dotenv import load_dotenv
import os
import requests

load_dotenv()

TEMP_IMAGES_PATH = '.temp_images'
LAST_FM_API_KEY = os.getenv('LAST_FM_API_KEY')
LAST_FM_API_SECRET = os.getenv('LAST_FM_API_SECRET')
WHAPI_API_URL = os.getenv('WHAPI_API_URL')
WHAPI_TOKEN = os.getenv('WHAPI_TOKEN')
USERNAME = 'zeerafle'
SIZE = 770

print('Connecting to Last.fm...')
network = pylast.LastFMNetwork(api_key=LAST_FM_API_KEY, api_secret=LAST_FM_API_SECRET)
user = network.get_user(USERNAME)

print('Getting top track of the week...')
top_track = user.get_top_tracks(period=pylast.PERIOD_7DAYS, limit=1)[0]
track_title = top_track.item.title
artist_name = top_track.item.artist.name
album = top_track.item.get_album()
album_name = album.get_title()
album_cover_url = album.get_cover_image(size=pylast.SIZE_EXTRA_LARGE)
album_cover_url = album_cover_url.replace('300x300', f'{SIZE}x{SIZE}')

print(f"Top track of the week: {track_title} by {artist_name} from the album {album_name}")
print(f"Album cover: {album_cover_url}")

print('Getting Whatsapp contact...')
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {WHAPI_TOKEN}"
}
params = {'count': 100}
response = requests.get(f'{WHAPI_API_URL}contacts', params=params, headers=headers)
contacts = response.json()
contacts = [contact['id'] for contact in contacts['contacts']]

print('Updating Whatsapp status')
payload = {
    "media": album_cover_url,
    "contacts": ['62895704806187'],
    "caption": f"Currently obsessed with {track_title}\n{artist_name} - {album_name}",
    "width": 770,
    "height": 770
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {WHAPI_TOKEN}"
}

response = requests.post(f'{WHAPI_API_URL}stories', json=payload, headers=headers)

if response.status_code != 200:
    print('Failed to update Whatsapp status')
    print(response.text)
print('Whatsapp status updated')
