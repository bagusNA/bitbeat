from PySide6.QtCore import QObject, Slot

from services.main import Service
from view_models.main import ViewModel
from views.main import View
from models.Song import Song


class FavouriteController(QObject):
    def __init__(self,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        super().__init__()

        # self._view = view
        self.service = service
        self.view_model = view_model.index

    @Slot(Song)
    def on_song_item_clicked(self, song: Song):
        self.service.audio_player.search_song(song.url)
