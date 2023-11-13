from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from models.Song import Song
from ui.ui_home_view import Ui_home_view as Ui
from widgets.RecommendationList import RecommendationList


class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

        self.recently_played_recommendation: RecommendationList | None = None
        self.latest_favourites_recommendation: RecommendationList | None = None

    def bind(self, controller):
        self._controller = controller.home

        self.ui.input_search.textChanged.connect(self._controller.change_search_query)
        self.ui.btn_search.clicked.connect(self._controller.on_search)
        self._controller.service.library.favourited_songs_changed.connect(self.on_favourites_changed)

        self.after_bind()

    def after_bind(self):
        self.recently_played_recommendation = RecommendationList(
            "Recently Played",
            self._controller.service.library.get_recent_songs()
        )

        self.latest_favourites_recommendation = RecommendationList(
            "Latest Favourites",
            self._controller.service.library.get_favourited_songs(limit=4)
        )

        self.ui.view_slot.addWidget(self.recently_played_recommendation)
        self.ui.view_slot.addWidget(self.latest_favourites_recommendation)

    @Slot(Song)
    def on_favourites_changed(self, changed_song: Song):
        if changed_song.is_favourite:
            self.latest_favourites_recommendation.add_song(changed_song)
        else:
            self.latest_favourites_recommendation.remove_song(changed_song)

    @Slot(str)
    def on_search_query_changed(self, value: str) -> None:
        self.ui.input_search.setText(value)
