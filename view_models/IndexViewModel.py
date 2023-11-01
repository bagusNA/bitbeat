from PySide6.QtCore import QObject, Signal
from models.Song import Song
from services.main import Service


class IndexViewModel(QObject):
    search_query_changed = Signal(str)

    def __init__(self, service: Service):
        super().__init__()
        self._player_service = service.audio_player

        self._search_query = ''

        self._player_service.on_song_change(self.emit_current_song)

    @property
    def search_query(self):
        return self._search_query

    @search_query.setter
    def search_query(self, query: str) -> None:
        self._search_query = query
        self.search_query_changed.emit(query)

    def emit_current_song(self):
        song = self._player_service.current_song
        self.current_song_changed.emit(song)
