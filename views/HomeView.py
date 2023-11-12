from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ui.ui_home_view import Ui_home_view as Ui
from widgets.RecommendationList import RecommendationList


class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

        self.recently_played_recommendation = None
        self.latest_favourites_recommendation = None

    def bind(self, controller):
        self._controller = controller.home

        self.ui.input_search.textChanged.connect(self._controller.change_search_query)
        self.ui.btn_search.clicked.connect(self._controller.on_search)

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

    @Slot(str)
    def on_search_query_changed(self, value: str) -> None:
        self.ui.input_search.setText(value)
