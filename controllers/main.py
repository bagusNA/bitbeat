from controllers.HomeController import HomeController
from controllers.FavouriteController import FavouriteController
from controllers.LyricsController import LyricsController
from view_models.main import ViewModel
from views.main import View
from services.main import Service


class Controller:
    def __init__(self,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        self.view_model = view_model
        self.view = view
        self.service = service

        self.home = HomeController(self, self.view_model, self.view, self.service)
        self.favourite = FavouriteController(self, self.view_model, self.view, self.service)
        self.lyrics = LyricsController(self, self.view_model, self.view, self.service)

    def start(self):
        self.view.start()

    def switch_view(self, name):
        if name == 'lyrics':
            self.view.layout.show_queue(False)
        else:
            self.view.layout.show_queue()

        return self.view.switch(name)

    def switch_to_home(self):
        return self.switch_view('home')

    def switch_to_playlist(self):
        return self.switch_view('playlist')

    def switch_to_favourite(self):
        return self.switch_view('favourite')

    def switch_to_setting(self):
        return self.switch_view('setting')

    def switch_to_lyrics(self):
        return self.switch_view('lyrics')
