from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from models.Song import Song
from utils.utils import Font
from widgets.SongCard import SongCard


class RecommendationList(QWidget):
    def __init__(self, title: str, songs: list[Song]):
        super(RecommendationList, self).__init__()

        self.container_layout = QVBoxLayout(self)
        self.song_container = QWidget()
        self.song_container_layout = QHBoxLayout()
        self.title = QLabel(title)

        Font.set_font_size(self.title, 15)

        for song in songs:
            self.song_container_layout.addWidget(SongCard(song))

        self.song_container_layout.setContentsMargins(0, 0, 0, 0)
        self.song_container_layout.setSpacing(0)
        self.song_container_layout.addStretch(0)

        self.song_container.setLayout(self.song_container_layout)

        self.container_layout.addWidget(self.title)
        self.container_layout.addWidget(self.song_container)
        self.setLayout(self.container_layout)
