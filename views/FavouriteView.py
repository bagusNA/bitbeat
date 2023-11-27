from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ui.ui_favourite_view import Ui_favourite_view as Ui
from widgets.FavouriteListItem import FavouriteListItem
from models.Song import Song


class FavouriteView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)
        self.song_list = []

    def bind(self, controller):
        self._controller = controller.favourite
        self._controller.service.library.favourited_songs_changed.connect(self.on_favourited_song_change)

        self.build_list()

    def on_show(self):
        pass

    def on_leave(self):
        pass

    def build_list(self):
        self.song_list = self._controller.service.library.get_favourited_songs()

        for index, song in enumerate(self.song_list):
            self.add_list_item(song, index)

    def add_list_item(self, song: Song, index: int = 0) -> None:
        song_item = FavouriteListItem(song)
        self.ui.favourite_list.insertWidget(index, song_item)

        song_item.clicked.connect(self._controller.on_song_item_clicked)

    @Slot(Song)
    def on_favourited_song_change(self, changed_song: Song):
        if changed_song.is_favourite:
            self.add_list_item(changed_song)
            self.song_list.insert(0, changed_song)
            return

        index = self.song_list.index(changed_song)
        self.song_list.pop(index)

        item = self.ui.favourite_list.takeAt(index)
        item.widget().deleteLater()
