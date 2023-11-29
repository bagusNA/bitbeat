from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QPainter, Qt, QBrush, QColor
from PySide6.QtWidgets import QLabel

from models.Song import Song


class AlbumCover(QLabel):
    SIZE_NORMAL = 64
    SIZE_LARGE = 96
    SIZE_EXTRA_LARGE = 124

    def __init__(self, img_path: str | bytes, size=SIZE_NORMAL, radius: int = 8):
        super(AlbumCover, self).__init__()

        self.image = None
        self.radius = radius
        self.size = size
        self.scaled_album_cover = None

        self.brush = QBrush()

        self.rounded_pixmap = QPixmap(self.size, self.size)
        self.clear()

        self.painter = QPainter(self.rounded_pixmap)

        self.set_image(img_path)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __del__(self):
        self.painter.end()

    def set_image(self, img_path: str | bytes):
        if type(img_path) is bytes:
            self.image = QPixmap()
            self.image.loadFromData(img_path)
        else:
            self.image = QPixmap(img_path)

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
