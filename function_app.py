import logging
import azure.functions as func
import datetime
import pylast

from file_utils import read_current_obsession, write_current_obsession
from lastfm_utils import get_top_track
from whatsapp_utils import update_whatsapp_status

app = func.FunctionApp()


@app.timer_trigger(schedule="0 0 0 */7 * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def StoryUpdate(myTimer: func.TimerRequest) -> None:
    logging.info('Python timer trigger function ran at %s', datetime.datetime.utcnow)
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Getting top track of the week...')
    top_track = get_top_track('zeerafle')
    track_title = top_track.item.title

    logging.info('Checking if the current obsession is the same as the last one...')
    if track_title == read_current_obsession():
        logging.info('Current obsession is the same as the last one. Exiting...')
        return

    logging.info('Save current obsession data')
    write_current_obsession(track_title)

    logging.info('Getting track details...')
    artist_name = top_track.item.artist.name
    album = top_track.item.get_album()
    album_name = album.get_title()
    album_cover_url = album.get_cover_image(size=pylast.SIZE_EXTRA_LARGE)
    album_cover_url = album_cover_url.replace('300x300', '770x770')

    logging.info(f"Top track of the week: {track_title} by {artist_name} from the album {album_name}")
    logging.info(f'Updating Whatsapp status')
    if update_whatsapp_status(album_cover_url, f"Currently obsessed with {track_title}\n{artist_name} - {album_name}"):
        logging.info('Whatsapp status updated')
    else:
        logging.info('Failed to update Whatsapp status')
