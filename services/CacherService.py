from __future__ import annotations
import os
from urllib.request import urlopen

from PySide6.QtCore import QObject, QSize, Qt, QRect
from PySide6.QtGui import QPixmap

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.Song import Song


class CacherService(QObject):
    CACHE_DIR = './cache'
    IMAGE_CACHE_SIZE = 256

    def __init__(self):
        super(CacherService, self).__init__()

    @classmethod
    def image_from_song(cls, song: Song) -> str:
        file_path = cls.filepath(song.id)

        if not os.path.isfile(file_path):
            cls.create_image_cache(song)

        return file_path

    @classmethod
    def create_image_cache(cls, song: Song):
        album_cover = QPixmap()

        img_data = urlopen(song.thumbnail_url).read()
        album_cover.loadFromData(img_data)

        cached_album_cover = album_cover.scaled(
            QSize(cls.IMAGE_CACHE_SIZE, cls.IMAGE_CACHE_SIZE),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        cropped_size = QRect(
            (cached_album_cover.width() - cls.IMAGE_CACHE_SIZE) / 2,
            0,
            cls.IMAGE_CACHE_SIZE,
            cls.IMAGE_CACHE_SIZE
        )

        cropped_img = cached_album_cover.copy(cropped_size)
        cropped_img.save(cls.filepath(song.id))

    @classmethod
    def filepath(cls, name: str) -> str:
        return f"{cls.CACHE_DIR}/{name}.png"
