from urllib.request import urlopen
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow, QPushButton
from PySide6.QtGui import QPixmap

from ui.ui_mainwindow import Ui_MainWindow
from models.Song import Song
from utils.utils import seconds_to_minutes

from widgets.QueueListWidget import QueueListWidget

class IndexView(QMainWindow):
    def __init__(self):
        super().__init__()

        self._controller = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_pause.setVisible(False)

    def bind(self, controller):
        self._controller = controller.index

        self._controller.player_service.current_song_changed.connect(self.on_song_change)
        self._controller.player_service.queue_changed.connect(self.on_queue_change)
        self._controller.player_service.playback_position_changed.connect(self.on_playback_position_changed)
        self._controller.player_service.playback_percent_changed.connect(self.on_playback_percent_changed)

        self.ui.input_search.textChanged.connect(self._controller.change_search_query)
        self.ui.btn_search.clicked.connect(self._controller.on_search)
        self.ui.btn_play.clicked.connect(self._controller.on_play_toggle)
        self.ui.btn_pause.clicked.connect(self._controller.on_play_toggle)
        self.ui.btn_previous.clicked.connect(self._controller.on_previous)
        self.ui.btn_next.clicked.connect(self._controller.on_next)

    @Slot(str)
    def on_search_query_changed(self, value: str) -> None:
        self.ui.input_search.setText(value)

    @Slot(Song)
    def on_song_change(self, song: Song) -> None:
        self.ui.song_title_label.setText(song.title)
        self.ui.song_artist_label.setText(song.artist)
        self.ui.total_duration_label.setText(song.duration_formatted)

        self.set_album_cover(song.thumbnail_url)

    @Slot(list)
    def on_queue_change(self, songs: list[Song]) -> None:
        self.build_queue(songs)

    @Slot(int)
    def on_playback_position_changed(self, seconds: int) -> None:
        time = seconds_to_minutes(seconds)
        self.ui.current_duration_label.setText(time)

    @Slot(int)
    def on_playback_percent_changed(self, percent: int) -> None:
        self.ui.playback_slider.setValue(percent)

    def toggle_play_button(self, is_playing: bool) -> None:
        if (is_playing):
            self.ui.btn_play.setVisible(False)
            self.ui.btn_pause.setVisible(True)
        else:
            self.ui.btn_play.setVisible(True)
            self.ui.btn_pause.setVisible(False)

    def set_album_cover(self, url: str) -> None:
        img_data = urlopen(url).read()

        album_cover = QPixmap()
        album_cover.loadFromData(img_data)
        scaled_album_cover = album_cover.scaled(
            self.ui.album_cover.size(),
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        self.ui.album_cover.setPixmap(scaled_album_cover)

    def build_queue(self, queue: list[Song]):
        container = self.ui.queue_list
        self.remove_all_widgets(container)

        for index, song in enumerate(queue):
            btn = QueueListWidget(text=song.title)
            btn.clicked.connect(lambda *args, idx=index: self._controller.on_play_on_index(idx))
            container.addWidget(btn)

    # Utilities
    def remove_all_widgets(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
