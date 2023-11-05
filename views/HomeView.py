from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from ui.ui_home_view import Ui_home_view as Ui


class HomeView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

    def bind(self, controller):
        self._controller = controller.home

        self.ui.input_search.textChanged.connect(self._controller.change_search_query)
        self.ui.btn_search.clicked.connect(self._controller.on_search)

    @Slot(str)
    def on_search_query_changed(self, value: str) -> None:
        self.ui.input_search.setText(value)
