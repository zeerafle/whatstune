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
