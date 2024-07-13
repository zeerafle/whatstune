import pylast
from dotenv import load_dotenv
import os
import requests
from imagedominantcolour import DominantColour

load_dotenv()

TEMP_IMAGES_PATH = '.temp_images'
LAST_FM_API_KEY = os.getenv('LAST_FM_API_KEY')
LAST_FM_API_SECRET = os.getenv('LAST_FM_API_SECRET')
WHAPI_API_URL = os.getenv('WHAPI_API_URL')
WHAPI_TOKEN = os.getenv('WHAPI_TOKEN')
USERNAME = 'zeerafle'

print('Connecting to Last.fm...')
network = pylast.LastFMNetwork(api_key=LAST_FM_API_KEY, api_secret=LAST_FM_API_SECRET)
user = network.get_user(USERNAME)

print('Getting top track of the week...')
top_track = user.get_top_tracks(period=pylast.PERIOD_7DAYS, limit=1)[0]
track_title = top_track.item.title
artist_name = top_track.item.artist.name
album = top_track.item.get_album()
album_name = album.get_title()
album_cover_url_small = album.get_cover_image(size=pylast.SIZE_SMALL)
album_cover_url_medium = album.get_cover_image(size=pylast.SIZE_MEDIUM)

print(f"Top track of the week: {track_title} by {artist_name} from the album {album_name}")

print('Downloading album cover...')
os.makedirs(TEMP_IMAGES_PATH, exist_ok=True)
response = requests.get(album_cover_url_small)
with open(os.path.join(TEMP_IMAGES_PATH, 'album_cover.jpg'), 'wb') as file:
    file.write(response.content)
print('Album cover downloaded as album_cover.jpg')

print('Getting dominant color of album cover...')
dominant_color = DominantColour(os.path.join(TEMP_IMAGES_PATH, 'album_cover.jpg'))
rgb_color = dominant_color.rgb
hex_color = '#%02x%02x%02x' % rgb_color
print(f'Dominant color of album cover: {hex_color}')

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
    "background_color": hex_color,
    "caption_color": "#FFFFFFFF",
    "media": album_cover_url_medium,
    "contacts": contacts,
    "font_type": "CALISTOGA_REGULAR",
    "caption": "Currently obsessed with " + track_title + " by " + artist_name + " from the album " + album_name
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
