import os

from peewee import SqliteDatabase
from dotenv import dotenv_values

from .Playlist import Playlist
from .Song import Song, PlaylistSong

env = dotenv_values('.env')
db = SqliteDatabase(env['DATABASE_PATH'])


class Migration:
    @staticmethod
    def start_or_skip():
        if os.path.exists(env['DATABASE_PATH']):
            return

        db.connect()
        db.create_tables([Song, Playlist, PlaylistSong])
