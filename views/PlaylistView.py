from PySide6.QtWidgets import QWidget

from ui.ui_playlist_view import Ui_playlist_view as Ui


class PlaylistView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

    def bind(self, controller):
        pass

    def on_show(self):
        pass

    def on_leave(self):
        pass
