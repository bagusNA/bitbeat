from .HomeView import HomeView
from .LyricsView import LyricsView
from .PlaylistView import PlaylistView
from .FavouriteView import FavouriteView
from .SearchView import SearchView
from .SettingView import SettingView
from .layouts.MainLayout import MainLayout


class View:
    def __init__(self):
        self._current_view = None
        self.layout = MainLayout(self)

        self.views = {
            'home': HomeView(),
            'playlist': PlaylistView(),
            'favourite': FavouriteView(),
            'setting': SettingView(),
            'lyrics': LyricsView(),
            'search': SearchView(),
        }

        self.layout.register_views(self.views)

    def bind(self, controller):
        self.layout.bind(controller)

        for _, view in self.views.items():
            view.bind(controller)

    def switch(self, name):
        if self._current_view:
            self.views[self._current_view].on_leave()

        self.layout.switch_view(name)

        self.views[name].on_show()
        self._current_view = name

        if name == 'lyrics':
            self.layout.show_queue(False)
        else:
            self.layout.show_queue()

    def start(self):
        self.layout.show()
