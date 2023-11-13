from datetime import datetime
from peewee import *

# from services.CacherService import CacherService
from utils.utils import coalesce
from models.main import Model


class Playlist(Model):
    id = TextField(primary_key=True)
    title = TextField()
    creator = TextField()
    url = TextField()
    channel_url = TextField()
    last_played_at = TimestampField(null=True)
    imported_at = TimestampField(null=True)

    def load(self, playlist_info: dict) -> None:
        self.id = playlist_info.get('id')
        self.title = playlist_info.get('title')
        self.creator = coalesce(playlist_info.get('artist', None), playlist_info.get('channel', None), playlist_info['uploader'])
        self.url = playlist_info.get('webpage_url')
        self.channel_url = playlist_info.get('channel_url')
        self.imported_at = datetime.now()

    def update_last_played(self) -> None:
        self.last_played_at = datetime.now().timestamp()
        self.save()
