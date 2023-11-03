from PySide6.QtCore import QObject, Signal
from services.main import Service


class IndexViewModel(QObject):
    search_query_changed = Signal(str)

    def __init__(self, service: Service):
        super().__init__()
        self._player_service = service.audio_player

        self._search_query = ''

    @property
    def search_query(self):
        return self._search_query

    @search_query.setter
    def search_query(self, query: str) -> None:
        self._search_query = query
        self.search_query_changed.emit(query)
