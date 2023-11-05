import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase

from controllers.main import Controller
from view_models.main import ViewModel
from views.main import View
from services.main import Service
from models.Migration import Migration


class BitBeatMusicPlayer(QApplication):
    def __init__(self, sys_argv):
        super(BitBeatMusicPlayer, self).__init__(sys_argv)

        Migration.start_or_skip()

        self.service = Service()
        self.view_model = ViewModel(self.service)
        self.view = View()
        self.controller = Controller(self.view_model, self.view, self.service)

        self.view.bind(self.controller)
        self.controller.start()

        with open('./assets/stylesheet.qss', 'r') as file:
            style = file.read()
            self.setStyleSheet(style)

        self.setup_fonts()

    def setup_fonts(self):
        font_dir = "./assets/fonts"
        fonts = [
            'Nunito-Bold.ttf',
            'Nunito-BoldItalic.ttf',
            'Nunito-SemiBold.ttf'
            'Nunito-SemiBoldItalic.ttf',
            'Nunito-Regular.ttf',
            'Nunito-Italic.ttf',
            'Nunito-Light.ttf',
            'Nunito-LightItalic.ttf',
        ]

        for font in fonts:
            QFontDatabase.addApplicationFont(f"{font_dir}/{font}")


if __name__ == '__main__':
    app = BitBeatMusicPlayer(sys.argv)
    sys.exit(app.exec())
