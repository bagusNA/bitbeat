from PySide6.QtCore import Signal
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStyleOption, QStyle

from models.Song import Song
from utils.utils import Font
from widgets.AlbumCover import AlbumCover
from widgets.MarqueeLabel import MarqueeLabel


class SongCard(QWidget):
    clicked = Signal(object)

    def __init__(self, song: Song):
        super(SongCard, self).__init__()

        self._song = song

        self.container_layout = QVBoxLayout(self)
        self.album_cover = AlbumCover(self._song.image_path, size=AlbumCover.SIZE_EXTRA_LARGE)
        self.song_title_label = MarqueeLabel(text=self._song.title, hover_parent=self)
        self.song_artist_label = MarqueeLabel(text=self._song.artist, hover_parent=self)

        self.song_title_label.setMaximumWidth(AlbumCover.SIZE_EXTRA_LARGE)
        self.song_artist_label.setMaximumWidth(AlbumCover.SIZE_EXTRA_LARGE)

        Font.set_font_size(self.song_artist_label, 11)
        Font.set_font_size(self.song_artist_label, 7)

        self.container_layout.addWidget(self.album_cover)
        self.container_layout.addWidget(self.song_title_label)
        self.container_layout.addWidget(self.song_artist_label)

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
        super(SongCard, self).paintEvent(event)

        opt = QStyleOption()
        opt.initFrom(self)

        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)
