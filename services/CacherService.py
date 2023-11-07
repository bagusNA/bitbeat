from urllib.request import urlopen

from PySide6.QtCore import QObject, QSize, Qt
from PySide6.QtGui import QPixmap

from models.Song import Song


class CacherService(QObject):
    CACHE_DIR = './cache'

    def __init__(self):
        super(CacherService, self).__init__()

    def image_from_song(self, song: Song, size: QSize = None) -> QPixmap:
        file_path = f"{self.CACHE_DIR}/{song.id}.png"

        album_cover = QPixmap()
        cache_exist = album_cover.load(file_path)

        if cache_exist:
            return album_cover

        img_data = urlopen(song.thumbnail_url).read()
        album_cover.loadFromData(img_data)

        scaled_album_cover = album_cover.scaled(
            size or QSize(64, 64),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        scaled_album_cover.save(file_path)

        return scaled_album_cover
