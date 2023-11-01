from enum import Enum
from utils.utils import coalesce, seconds_to_minutes


class Status(Enum):
    NOT_PLAYED = 0
    CURRENTLY_PLAYED = 1
    HAS_PLAYED = 2


class Song(object):
    def __init__(self,
                 song_info: dict,
                 status: Status = Status.NOT_PLAYED
                 ) -> None:
        self.id = song_info.get('id')
        self.title = song_info.get('title')
        self.artist = coalesce(song_info.get('artist', None), song_info.get('channel', None), song_info['uploader'])
        self.url = song_info.get('webpage_url')
        self.audio_url = song_info.get('audio_url')
        self.duration = song_info.get('duration')
        self.duration_formatted = seconds_to_minutes(self.duration)
        self.thumbnail_url = song_info.get('thumbnail')
        self.formats = song_info.get('formats')
        self.view_count = song_info.get('view_count')
        self.upload_date = song_info.get('upload_date')
        self.channel_url = song_info.get('channel_url')
        self.status = status
