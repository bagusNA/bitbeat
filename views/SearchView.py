from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from models.Video import Video
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
        self._controller.view_model.search_query_changed.connect(self.on_search_query_changed)

        self.ui.input_search.textChanged.connect(self._controller.change_search_query)
        self.ui.input_search.returnPressed.connect(self._controller.on_search)
        self.ui.btn_search.clicked.connect(self._controller.on_search)

    def on_show(self):
        pass

    def on_leave(self):
        pass

    @Slot(str)
    def on_search_query_changed(self, value: str) -> None:
        self.ui.input_search.setText(value)

    @Slot(object)
    def on_search_result_fetched(self, videos: list[Video]):
        self.clear_item()

        for song in videos:
            self.build_result_item(song)

    def build_result_item(self, video: Video):
        list_item = SearchListItem(video)
        self.ui.search_container.addWidget(list_item)

        list_item.clicked.connect(self._controller.on_video_item_clicked)

    def clear_item(self):
        utils.remove_all_widgets(self.ui.search_container)
