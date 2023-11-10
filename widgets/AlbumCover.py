from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QPainter, Qt, QBrush, QColor
from PySide6.QtWidgets import QLabel

from models.Song import Song


class AlbumCover(QLabel):
    SIZE_LARGE = 96
    SIZE_NORMAL = 64

    def __init__(self, song: Song, size=SIZE_NORMAL, radius: int = 8):
        super(AlbumCover, self).__init__()

        self.image = None
        self.radius = radius
        self.size = size
        self.scaled_album_cover = None

        self.brush = QBrush()

        self.rounded_pixmap = QPixmap(self.size, self.size)
        self.clear()

        self.painter = QPainter(self.rounded_pixmap)

        self.set_song(song)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __del__(self):
        self.painter.end()

    def set_song(self, song: Song):
        self.image = QPixmap(song.image_path)

        self.scaled_album_cover = self.image.scaled(
            QSize(self.size, self.size),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        self.clear()

        self.brush.setTexture(self.scaled_album_cover)

        self.painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.painter.setBrush(self.brush)
        self.painter.setPen(Qt.PenStyle.NoPen)
        self.painter.drawRoundedRect(self.rounded_pixmap.rect(), self.radius, self.radius)

        self.setPixmap(self.rounded_pixmap)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def clear(self):
        self.rounded_pixmap.fill(QColor("transparent"))
