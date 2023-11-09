from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent, QPixmap, QPaintEvent, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QStyleOption, QStyle
from models.Song import Song
from utils.utils import Font
from widgets.AlbumCover import AlbumCover


class FavouriteListItem(QWidget):
    clicked = Signal(object)

    def __init__(self, song: Song, img: QPixmap, parent=None):
        super(FavouriteListItem, self).__init__(parent)

        self._song = song

        self.album_cover = AlbumCover(img)
        self.title_label = QLabel(song.title)
        self.artist_label = QLabel(song.artist)

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
        self.setProperty("pressed", True)
        self.style().polish(self)
        self.style().unpolish(self)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.setProperty("pressed", False)
        self.style().polish(self)
        self.style().unpolish(self)

        self.clicked.emit(self._song)

    def paintEvent(self, event: QPaintEvent) -> None:
        super(FavouriteListItem, self).paintEvent(event)

        opt = QStyleOption()
        opt.initFrom(self)

        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
