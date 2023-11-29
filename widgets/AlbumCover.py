from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QPixmap, QPainter, Qt, QBrush, QColor
from PySide6.QtWidgets import QLabel


class AlbumCoverWorker(QThread):
    image_created = Signal(QPixmap)

    def __init__(self, album):
        super(AlbumCoverWorker, self).__init__()
        self._album = album
        self._image = None
        self._scaled_album_cover = None

        self._rounded_pixmap = QPixmap(self._album.size, self._album.size)
        self._brush = QBrush()

        self._painter = QPainter(self._rounded_pixmap)

    def clear(self):
        self._rounded_pixmap.fill(QColor("transparent"))

    def run(self) -> None:
        if type(self._album.image_source) is bytes:
            self._image = QPixmap()
            self._image.loadFromData(self._album.image_source)
        else:
            self._image = QPixmap(self._album.image_source)

        self._scaled_album_cover = self._image.scaled(
            QSize(self._album.size, self._album.size),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        self.clear()

        self._brush.setTexture(self._scaled_album_cover)

        self._painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        self._painter.setBrush(self._brush)
        self._painter.setPen(Qt.PenStyle.NoPen)
        self._painter.drawRoundedRect(self._rounded_pixmap.rect(), self._album.radius, self._album.radius)

        self.image_created.emit(self._rounded_pixmap)


class AlbumCover(QLabel):
    SIZE_NORMAL = 64
    SIZE_LARGE = 96
    SIZE_EXTRA_LARGE = 124

    def __init__(self, img_path: str | bytes, size=SIZE_NORMAL, radius: int = 8):
        super(AlbumCover, self).__init__()

        self.image_source = None
        self.image = None
        self.radius = radius
        self.size = size

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._worker = AlbumCoverWorker(self)
        self._worker.image_created.connect(self.on_image_created)

        self.set_image(img_path)

    def set_image(self, img_source: str | bytes):
        self.image_source = img_source
        self._worker.start()

    @Slot(QPixmap)
    def on_image_created(self, image: QPixmap):
        self.setPixmap(image)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
