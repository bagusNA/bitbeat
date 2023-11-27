from PySide6.QtWidgets import QWidget

from ui.ui_lyrics_view import Ui_lyrics_view as Ui


class LyricsView(QWidget):
    def __init__(self):
        super(LyricsView, self).__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

    def bind(self, controller):
        self._controller = controller.lyrics

