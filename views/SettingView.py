from PySide6.QtWidgets import QWidget

from ui.ui_setting_view import Ui_setting_view as Ui


class SettingView(QWidget):
    def __init__(self):
        super().__init__()

        self._controller = None

        self.ui = Ui()
        self.ui.setupUi(self)

    def bind(self, controller):
        pass

    def on_show(self):
        pass

    def on_leave(self):
        pass
