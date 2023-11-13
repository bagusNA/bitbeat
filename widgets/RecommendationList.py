import typing

from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from models.Song import Song
from utils.utils import Font
from widgets.SongCard import SongCard


class RecommendationList(QWidget):
    def __init__(self, title: str, songs: list[Song], clicked_callback: typing.Callable = None):
        super(RecommendationList, self).__init__()

        self._songs = []
        self._clicked_callback = clicked_callback

        self.container_layout = QVBoxLayout(self)
        self.song_container = QWidget()
        self.song_container_layout = QHBoxLayout()
        self.title = QLabel(title)

        Font.set_font_size(self.title, 15)

        self.song_container_layout.setContentsMargins(0, 0, 0, 0)
        self.song_container_layout.setSpacing(8)
        self.song_container_layout.addStretch()

        for song in songs:
            self.add_song(song, append=False)

        self.song_container.setLayout(self.song_container_layout)

        self.container_layout.addWidget(self.title)
        self.container_layout.addWidget(self.song_container)
        self.setLayout(self.container_layout)

    def add_song(self, song: Song, append: bool = True, unique: bool = True) -> None:
        index = 0 if append else self.song_container_layout.count() - 1

        if unique:
            try:
                existing_index = self._songs.index(song)
                self.remove_song_by_index(existing_index)
            except ValueError:
                pass

        song_card = SongCard(song)
        if self._clicked_callback is not None:
            song_card.clicked.connect(self._clicked_callback)

        self.song_container_layout.insertWidget(index, song_card)

        if append:
            self._songs.insert(0, song)
        else:
            self._songs.append(song)

    def remove_song(self, song: Song) -> None:
        index = self._songs.index(song)
        self.remove_song_by_index(index)

    def remove_song_by_index(self, index: int) -> None:
        song_item = self.song_container_layout.takeAt(index)
        song_item.widget().deleteLater()

        self._songs.pop(index)
