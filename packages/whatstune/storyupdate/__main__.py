import datetime

from file_utils import read_current_obsession, write_current_obsession
from lastfm_utils import get_top_track, get_track_details
from whatsapp_utils import update_whatsapp_status


def main(args):
    print('Python timer trigger function ran at %s', datetime.datetime.utcnow)

    top_track = get_top_track('zeerafle')
    track_title = top_track.item.title

    print('Checking if the current obsession is the same as the last one...')
    if track_title == read_current_obsession():
        print('Current obsession is the same as the last one. Exiting...')
        return

    print('Save current obsession data')
    write_current_obsession(track_title)

    print('Getting track details...')
    artist, album, album_cover_url = get_track_details(top_track)

    print(f"Top track of the week: {track_title} by {artist} from the album {album}")
    print(f'Updating Whatsapp status')
    if update_whatsapp_status(album_cover_url, f"Currently obsessed with {track_title}\n{artist} - {album}"):
        return {'body': f'Whatsapp story updated, {track_title} is the current obsession'}
    else:
        return {'body': 'Failed to update Whatsapp status'}
