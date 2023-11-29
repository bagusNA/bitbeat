from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QLabel
from youtube_search import YoutubeSearch

from ui.ui_search_view import Ui_search_view as Ui
from utils import utils
from widgets.SearchListItem import SearchListItem


class SearchView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

    def bind(self, controller):
        self._controller = controller.search
        self._controller.service.song_fetcher.search_result_fetched.connect(self.on_search_result_fetched)

    def on_show(self):
        self.clear_item()

    def on_leave(self):
        self.clear_item()

    @Slot(object)
    def on_search_result_fetched(self, result: YoutubeSearch):
        for song in result.videos:
            print(song['thumbnails'][0])
            self.build_result_item(song)

    def build_result_item(self, video: dict):
        list_item = SearchListItem(video)
        self.ui.search_container.addWidget(list_item)

    def clear_item(self):
        utils.remove_all_widgets(self.ui.search_container)
