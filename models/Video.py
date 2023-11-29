from peewee import *

from services.CacherService import CacherService
from utils.utils import coalesce
from .main import Model


class Video(Model):
    id = TextField(primary_key=True)
    title = TextField()
    artist = TextField()
    url = TextField()
    channel_url = TextField()
    thumbnail_url = TextField()

    def load(self, video_info: dict) -> None:
        self.id = video_info.get('id')
        self.title = video_info.get('title')
        self.artist = coalesce(video_info.get('artist', None), video_info.get('channel', None), video_info.get('uploader', None))
        self.url = video_info.get('webpage_url')
        self.channel_url = video_info.get('channel_url')
        self.thumbnail_url = video_info.get('thumbnails')[0]

    @property
    def image_path(self):
        return CacherService.image_from_song(self)
