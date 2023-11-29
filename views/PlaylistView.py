from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from models.Playlist import Playlist
from ui.ui_playlist_view import Ui_playlist_view as Ui
from widgets.PlaylistListItem import PlaylistListItem


class PlaylistView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)
        self._playlist_list = []

    def bind(self, controller):
        self._controller = controller.playlist
        self._controller.service.library.playlist_imported.connect(self.on_playlist_import)

        self.build_list()

    def on_show(self):
        pass

    def on_leave(self):
        pass

    @Slot(Playlist)
    def on_playlist_import(self, imported_playlist: Playlist):
        self.add_list_item(imported_playlist)
        self._playlist_list.insert(0, imported_playlist)

    def build_list(self):
        self._playlist_list = self._controller.service.library.get_recent_playlist(limit=25)

        for index, playlist in enumerate(self._playlist_list):
            self.add_list_item(playlist, index)

    def add_list_item(self, playlist: Playlist, index: int = 0) -> None:
        playlist_widget = PlaylistListItem(playlist)
        self.ui.playlist_list.insertWidget(index, playlist_widget)

        playlist_widget.clicked.connect(self._controller.on_playlist_item_clicked)
