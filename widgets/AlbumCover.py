from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, QPainter, Qt, QBrush, QColor
from PySide6.QtWidgets import QLabel


class AlbumCover(QLabel):
    SIZE_LARGE = 96
    SIZE_NORMAL = 64

    def __init__(self, image: QPixmap, size=SIZE_NORMAL, radius: int = 8):
        super(AlbumCover, self).__init__()

        self.image = image
        self.radius = radius

        self.rounded_pixmap = QPixmap(size, size)
        self.rounded_pixmap.fill(QColor("transparent"))

        self.painter = QPainter(self.rounded_pixmap)
        self.painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.painter.setBrush(QBrush(image))
        self.painter.setPen(Qt.PenStyle.NoPen)
        self.painter.drawRoundedRect(self.rounded_pixmap.rect(), self.radius, self.radius)

        self.setPixmap(self.rounded_pixmap)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def __del__(self):
        self.painter.end()
