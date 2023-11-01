import sys
from PySide6.QtWidgets import QApplication
from controllers.main import Controller
from view_models.main import ViewModel
from views.main import View
from services.main import Service


class BitBeatMusicPlayer(QApplication):
    def __init__(self, sys_argv):
        super(BitBeatMusicPlayer, self).__init__(sys_argv)

        self.service = Service()
        self.view_model = ViewModel(self.service)
        self.view = View()
        self.controller = Controller(self.view_model, self.view, self.service)

        self.view.bind(self.controller)
        self.controller.start()

        with open('./assets/stylesheet.qss', 'r') as file:
            style = file.read()
            self.setStyleSheet(style)


if __name__ == '__main__':
    app = BitBeatMusicPlayer(sys.argv)
    sys.exit(app.exec())
