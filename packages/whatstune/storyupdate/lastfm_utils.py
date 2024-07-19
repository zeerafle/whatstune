import pylast
import os


def get_network():
    api_key = os.getenv('LAST_FM_API_KEY')
    api_secret = os.getenv('LAST_FM_API_SECRET')
    return pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret)


def get_top_track(username):
    network = get_network()
    user = network.get_user(username)
    top_track = user.get_top_tracks(period=pylast.PERIOD_7DAYS, limit=1)[0]
    return top_track


def get_track_details(track: pylast.TopItem):
    artist_name = track.item.artist.name
    album = track.item.get_album()
    album_name = album.get_title()
    album_cover_url = album.get_cover_image(size=pylast.SIZE_EXTRA_LARGE)
    album_cover_url = album_cover_url.replace('300x300', '770x770')
    return artist_name, album_name, album_cover_url
