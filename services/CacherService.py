from urllib.request import urlopen

from PySide6.QtCore import QObject, QSize, Qt, QRect
from PySide6.QtGui import QPixmap

from models.Song import Song


class CacherService(QObject):
    CACHE_DIR = './cache'
    IMAGE_CACHE_SIZE = 256

    def __init__(self):
        super(CacherService, self).__init__()

    def image_from_song(self, song: Song, size: QSize = None) -> QPixmap:
        if size is None:
            size = QSize(64, 64)

        file_path = self.filepath(song.id)

        album_cover = QPixmap()
        cache_exist = album_cover.load(file_path)

        if not cache_exist:
            img_data = urlopen(song.thumbnail_url).read()
            album_cover.loadFromData(img_data)

            self.create_image_cache(album_cover, song.id)

        scaled_album_cover = album_cover.scaled(
            size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        return scaled_album_cover

    def create_image_cache(self, img: QPixmap, name: str):
        cached_album_cover = img.scaled(
            QSize(self.IMAGE_CACHE_SIZE, self.IMAGE_CACHE_SIZE),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        cropped_size = QRect(
            (cached_album_cover.width() - self.IMAGE_CACHE_SIZE) / 2,
            0,
            self.IMAGE_CACHE_SIZE,
            self.IMAGE_CACHE_SIZE
        )

        cropped_img = cached_album_cover.copy(cropped_size)
        cropped_img.save(self.filepath(name))

    def filepath(self, name: str):
        return f"{self.CACHE_DIR}/{name}.png"
