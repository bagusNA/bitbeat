from PySide6.QtCore import QObject

from dotenv import dotenv_values
from lyricsgenius import Genius
from lyricsgenius.types import Song


class LyricsService(QObject):
    def __init__(self, service):
        super(LyricsService, self).__init__()

        self._service = service

        env = dotenv_values('.env')
        self.genius = Genius(env['GENIUS_ACCESS_TOKEN'])

    def search_by_title(self, title: str):
        song: Song = self.genius.search_song(title)

        return song.lyrics

    def search_current_song(self):
        song = self._service.audio_player.current_song

        return self.search_by_title(song.title)
