from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from models.Song import Song
from utils.utils import Font


class FavouriteListItemWidget(QWidget):
    clicked = Signal(object)

    def __init__(self, song: Song, parent=None):
        super(FavouriteListItemWidget, self).__init__(parent)

        self._song = song

        self.album_cover = QLabel("Album")
        self.title_label = QLabel(song.title)
        self.artist_label = QLabel(song.artist)

        self.album_cover.setFixedSize(64, 64)
        Font.set_font_size(self.title_label, 11)
        Font.set_font_size(self.artist_label, 8)

        self.text_layout = QVBoxLayout()
        self.text_layout.addWidget(self.title_label)
        self.text_layout.addWidget(self.artist_label)
        self.text_layout.setSpacing(0)

        self.container_layout = QHBoxLayout()
        self.container_layout.addWidget(self.album_cover, 0)
        self.container_layout.addLayout(self.text_layout, 1)
        self.container_layout.setSpacing(16)
        self.setLayout(self.container_layout)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit(self._song)
