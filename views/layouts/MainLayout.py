from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from ui.ui_mainwindow import Ui_MainWindow
from models.Song import Song
from utils.utils import seconds_to_minutes, remove_all_widgets
from widgets.AlbumCover import AlbumCover
from widgets.QueueListItem import QueueListItem


class MainLayout(QMainWindow):
    def __init__(self, base_view):
        super().__init__()

        self._base_controller = None
        self._controller = None
        self._base_view = base_view

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.album_cover = None

        self.views = {}

        self.prepare_ui()

    def bind(self, controller):
        self._base_controller = controller
        self._controller = controller.home

        self._controller.player_service.current_song_changed.connect(self.on_song_change)
        self._controller.player_service.queue_changed.connect(self.on_queue_change)
        self._controller.player_service.playback_status_changed.connect(self.on_playback_status_changed)
        self._controller.player_service.playback_position_changed.connect(self.on_playback_position_changed)
        self._controller.player_service.playback_percent_changed.connect(self.on_playback_percent_changed)
        self._controller.player_service.playback_volume_changed.connect(self.on_playback_volume_changed)
        self._controller.player_service.playback_muted_changed.connect(self.on_playback_muted_changed)
        self._controller.view_model.song_favourite_changed.connect(self.on_song_favourite_changed)

        self.ui.btn_play.clicked.connect(self._controller.on_play_toggle)
        self.ui.btn_pause.clicked.connect(self._controller.on_play_toggle)
        self.ui.btn_previous.clicked.connect(self._controller.on_previous)
        self.ui.btn_next.clicked.connect(self._controller.on_next)
        self.ui.btn_favourited.clicked.connect(self._controller.on_song_favourite_toggled)
        self.ui.btn_not_favourited.clicked.connect(self._controller.on_song_favourite_toggled)
        self.ui.btn_lyrics.clicked.connect(self._base_controller.switch_to_lyrics)
        self.ui.btn_volume.clicked.connect(self._controller.on_volume_toggle_mute)
        self.ui.btn_volume_muted.clicked.connect(self._controller.on_volume_toggle_mute)
        self.ui.playback_slider.valueChanged.connect(self._controller.on_playback_scrobble)
        self.ui.volume_slider.valueChanged.connect(self._controller.on_volume_change)

        self.ui.btn_home.clicked.connect(self._base_controller.switch_to_home)
        self.ui.btn_playlist.clicked.connect(self._base_controller.switch_to_playlist)
        self.ui.btn_favourite.clicked.connect(self._base_controller.switch_to_favourite)
        self.ui.btn_setting.clicked.connect(self._base_controller.switch_to_setting)

    def prepare_ui(self):
        self.ui.btn_pause.setVisible(False)
        self.ui.btn_volume_muted.setVisible(False)
        self.ui.btn_favourited.setVisible(False)
        self.ui.playback_slider.setTracking(False)

    def register_views(self, views: dict) -> None:
        self.views = views

        for name, view in views.items():
            self.ui.view_slot.addWidget(view)

        self.set_view(0)

    def set_view(self, index: int = 0):
        self.ui.view_slot.setCurrentIndex(index)

    def switch_view(self, view_name):
        selected_index = list(self.views.keys()).index(view_name)
        self.set_view(selected_index)

    def show_queue(self, show: bool = True):
        if show:
            self.ui.queue_widget.show()
        else:
            self.ui.queue_widget.hide()

    @Slot(Song)
    def on_song_change(self, song: Song) -> None:
        self.ui.song_title_label.setText(song.title)
        self.ui.song_artist_label.setText(song.artist)
        self.ui.total_duration_label.setText(song.duration_formatted)

        self.ui.btn_favourited.setVisible(song.is_favourite)
        self.ui.btn_not_favourited.setVisible(not song.is_favourite)

        self.set_album_cover(song)

    @Slot(list)
    def on_queue_change(self, songs: list[Song]) -> None:
        length_time = sum(song.duration for song in songs)
        minutes, seconds = seconds_to_minutes(length_time, formatted=False)
        total_song = len(songs)

        self.ui.queue_length_info_label.setText(
            f"{total_song} song{'s' if total_song > 1 else ''}, {minutes} min {seconds} sec")

        self.build_queue(songs)

    @Slot(bool)
    def on_playback_status_changed(self, is_playing: bool) -> None:
        self.ui.btn_play.setVisible(not is_playing)
        self.ui.btn_pause.setVisible(is_playing)

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

    @Slot(bool)
    def on_song_favourite_changed(self, is_favourited: bool) -> None:
        self.ui.btn_favourited.setVisible(is_favourited)
        self.ui.btn_not_favourited.setVisible(not is_favourited)

    def set_album_cover(self, song: Song) -> None:
        if self.album_cover is not None:
            self.album_cover.set_image(song.image_path)
        else:
            self.album_cover = AlbumCover(song.image_path)

            self.ui.placeholder_album_cover.deleteLater()
            self.ui.song_info.insertWidget(0, self.album_cover)
            self.ui.song_info.setSpacing(12)
            self.ui.song_info.insertStretch(3)

    def build_queue(self, queue: list[Song]):
        container = self.ui.queue_list
        remove_all_widgets(container)

        for index, song in enumerate(queue):
            btn = QueueListItem(song)
            btn.clicked.connect(lambda *args, idx=index: self._controller.on_play_on_index(idx))
            container.addWidget(btn)
