from PySide6.QtCore import QObject, Slot
from ui.ui_mainwindow import Ui_MainWindow
from view_models.main import ViewModel
from views.main import View
from services.main import Service
from models.Song import Song


class IndexController(QObject):
    def __init__(self,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        super().__init__()

        self._view_model = view_model.index
        self._view = view.views['index']
        self._ui: Ui_MainWindow = view.ui('index')

        self._service = service
        self.player_service = self._service.audio_player

    @Slot(bool)
    def on_search(self):
        self.player_service.search_song(self._view_model.search_query)
        self._view.toggle_play_button(self.player_service.is_currently_playing)

    @Slot(bool)
    def on_play_toggle(self):
        self.player_service.toggle()
        self._view.toggle_play_button(self.player_service.is_currently_playing)

    @Slot(bool)
    def on_play(self):
        self.player_service.play()

    @Slot(int)
    def on_play_on_index(self, index):
        self.player_service.play(index)
        print(index)

    @Slot(bool)
    def on_pause(self):
        self.player_service.pause()

    @Slot(bool)
    def on_next(self):
        self.player_service.next()

    @Slot(bool)
    def on_previous(self):
        self.player_service.previous()

    @Slot(str)
    def change_search_query(self, value):
        self._view_model.search_query = value

    @Slot(int)
    def on_volume_change(self, value):
        self.player_service.playback_volume = value

    @Slot(bool)
    def on_volume_toggle_mute(self, _) -> None:
        self.player_service.playback_muted = not self.player_service.playback_muted
