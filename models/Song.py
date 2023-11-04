from datetime import datetime
from peewee import *

from utils.utils import coalesce, seconds_to_minutes
from .main import Model


class Song(Model):
    id = TextField(primary_key=True)
    title = TextField()
    artist = TextField()
    duration = IntegerField()
    url = TextField()
    channel_url = TextField()
    upload_date = TextField()
    is_favourite = BooleanField(default=False)
    last_played_at = TimestampField()

    def load(self, song_info: dict) -> None:
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

    def set_favourite(self, value: bool):
        self.is_favourite = value
        self.save()

    def toggle_favourite(self):
        return self.set_favourite(not self.is_favourite)

    def update_last_played(self):
        self.last_played_at = datetime.now().timestamp()
        self.save()
