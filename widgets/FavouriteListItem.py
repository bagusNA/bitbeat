from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStyleOption, QStyle
from models.Song import Song
from utils.utils import Font
from widgets.AlbumCover import AlbumCover
from widgets.MarqueeLabel import MarqueeLabel


class FavouriteListItem(QWidget):
    clicked = Signal(object)

    def __init__(self, song: Song, parent=None):
        super(FavouriteListItem, self).__init__(parent)

        self._song = song

        self.album_cover = AlbumCover(song.image_path)
        self.title_label = MarqueeLabel(text=song.title, hover_parent=self)
        self.artist_label = MarqueeLabel(text=song.artist, hover_parent=self)

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
