from urllib.request import urlopen
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap

from ui.ui_mainwindow import Ui_MainWindow
from models.Song import Song
from utils.utils import seconds_to_minutes, remove_all_widgets

from widgets.QueueListWidget import QueueListWidget


class IndexView(QMainWindow):
    def __init__(self):
        super().__init__()

        self._controller = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.prepare_ui()

    def bind(self, controller):
        self._controller = controller.index

        self._controller.player_service.current_song_changed.connect(self.on_song_change)
        self._controller.player_service.queue_changed.connect(self.on_queue_change)
        self._controller.player_service.playback_position_changed.connect(self.on_playback_position_changed)
        self._controller.player_service.playback_percent_changed.connect(self.on_playback_percent_changed)
        self._controller.player_service.playback_volume_changed.connect(self.on_playback_volume_changed)
        self._controller.player_service.playback_muted_changed.connect(self.on_playback_muted_changed)

        self.ui.input_search.textChanged.connect(self._controller.change_search_query)
        self.ui.btn_search.clicked.connect(self._controller.on_search)
        self.ui.btn_play.clicked.connect(self._controller.on_play_toggle)
        self.ui.btn_pause.clicked.connect(self._controller.on_play_toggle)
        self.ui.btn_previous.clicked.connect(self._controller.on_previous)
        self.ui.btn_next.clicked.connect(self._controller.on_next)
        self.ui.btn_volume.clicked.connect(self._controller.on_volume_toggle_mute)
        self.ui.btn_volume_muted.clicked.connect(self._controller.on_volume_toggle_mute)
        self.ui.playback_slider.valueChanged.connect(self._controller.on_playback_scrobble)
        self.ui.volume_slider.valueChanged.connect(self._controller.on_volume_change)

    def prepare_ui(self):
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_volume_muted.setVisible(False)
        self.ui.playback_slider.setTracking(False)

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

    # FIXME: Slider gets reverted back to position if user stays still for too long when dragging
    @Slot(int)
    def on_playback_percent_changed(self, percent: int) -> None:
        self.ui.playback_slider.setSliderPosition(percent)

    @Slot(int)
    def on_playback_volume_changed(self, percent: int) -> None:
        self.ui.volume_slider.setValue(percent)

    @Slot(bool)
    def on_playback_muted_changed(self, is_muted: bool) -> None:
        self.ui.volume_slider.setEnabled(not is_muted)
        self.ui.btn_volume.setVisible(not is_muted)
        self.ui.btn_volume_muted.setVisible(is_muted)

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
        remove_all_widgets(container)

        for index, song in enumerate(queue):
            btn = QueueListWidget(text=song.title)
            btn.clicked.connect(lambda *args, idx=index: self._controller.on_play_on_index(idx))
            container.addWidget(btn)
