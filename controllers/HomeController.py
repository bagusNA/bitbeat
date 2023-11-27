from __future__ import annotations
from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Slot

from models.Song import Song
from view_models.main import ViewModel
from views.main import View
from services.main import Service

if TYPE_CHECKING:
    from controllers.main import Controller


class HomeController(QObject):
    def __init__(self,
                 controller: Controller,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        super().__init__()

        self._controller = controller
        self._view = view
        self.service = service
        self.player_service = self.service.audio_player
        self.view_model = view_model.index

    @Slot(bool)
    def on_search(self):
        self.player_service.search_song(self.view_model.search_query)

    @Slot(str)
    def change_search_query(self, value):
        self.view_model.search_query = value

    @Slot(bool)
    def on_play_toggle(self):
        self.player_service.toggle()

    @Slot(bool)
    def on_play(self):
        self.player_service.play()

    @Slot(int)
    def on_play_on_index(self, index):
        self.player_service.play(index)

    @Slot(bool)
    def on_pause(self):
        self.player_service.pause()

    @Slot(bool)
    def on_next(self):
        self.player_service.next()

    @Slot(bool)
    def on_previous(self):
        self.player_service.previous()

    @Slot(int)
    def on_playback_scrobble(self, percent: int):
        self.player_service.move_playback_to(percent)

    @Slot(int)
    def on_volume_change(self, value):
        self.player_service.playback_volume = value

    @Slot(bool)
    def on_volume_toggle_mute(self, _) -> None:
        self.player_service.playback_muted = not self.player_service.playback_muted

    @Slot(bool)
    def on_song_favourite_toggled(self, _) -> None:
        current_song = self.player_service.current_song
        if not current_song:
            return

        self.service.library.toggle_song_favourite(current_song)
        self.view_model.song_favourite_changed.emit(current_song.is_favourite)

    @Slot(Song)
    def on_song_item_clicked(self, song: Song):
        self.service.audio_player.search_song(song.url)

    @Slot(bool)
    def on_btn_lyrics_clicked(self, _):
        self._view.layout.hide_queue()
