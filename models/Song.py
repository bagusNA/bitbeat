from datetime import datetime
from peewee import *

from services.CacherService import CacherService
from utils.utils import coalesce, seconds_to_minutes
from .Playlist import Playlist
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
    favourited_at = TimestampField(null=True)
    last_played_at = TimestampField(null=True)

    playlist = ManyToManyField(Playlist, backref='songs')

    _thumbnail_url = None

    def load(self, song_info: dict) -> None:
        self.id = song_info.get('id')
        self.title = song_info.get('title')
        self.artist = coalesce(song_info.get('artist', None), song_info.get('channel', None), song_info['uploader'])
        self.url = song_info.get('webpage_url')
        self.audio_url = song_info.get('audio_url')
        self.duration = song_info.get('duration')
        self.duration_formatted = seconds_to_minutes(self.duration)
        self._thumbnail_url = song_info.get('thumbnail')
        self.formats = song_info.get('formats')
        self.view_count = song_info.get('view_count')
        self.upload_date = song_info.get('upload_date')
        self.channel_url = song_info.get('channel_url')

    def set_favourite(self, value: bool):
        self.is_favourite = value
        self.favourited_at = datetime.now().timestamp() if self.is_favourite else None

        self.save()

    def toggle_favourite(self):
        return self.set_favourite(not self.is_favourite)

    def update_last_played(self):
        self.last_played_at = datetime.now().timestamp()
        self.save()

    @property
    def thumbnail_url(self):
        return coalesce(self._thumbnail_url, f"https://i.ytimg.com/vi/{self.id}/mqdefault.jpg")

    @property
    def image_path(self):
        return CacherService.image_from_song(self)


PlaylistSong = Song.playlist.get_through_model()
