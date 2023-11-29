from __future__ import annotations
from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Slot

from models.Video import Video
from services.main import Service
from utils import utils
from view_models.main import ViewModel
from views.main import View

if TYPE_CHECKING:
    from controllers.main import Controller


class SearchController(QObject):
    def __init__(self,
                 controller: Controller,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        super().__init__()

        self._controller = controller
        self._view = view
        self.service = service
        self.view_model = view_model.index

    @Slot(bool)
    def on_search(self):
        query = self.view_model.search_query

        if not utils.is_youtube_url(query):
            self.service.audio_player.search_song_query(query)
        else:
            self.service.audio_player.search_song(query)

    @Slot(object)
    def on_video_item_clicked(self, video: Video):
        url = utils.youtube_url_from_id(video.id)
        self.service.audio_player.search_song(url)

    @Slot(str)
    def change_search_query(self, value: str):
        self.view_model.search_query = value
