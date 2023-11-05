from .HomeView import HomeView
from .PlaylistView import PlaylistView
from .layouts.MainLayout import MainLayout


class View:
    def __init__(self):
        self.current_view = None
        self.layout = MainLayout(self)

        self.views = {
            'home': HomeView(),
            'playlist': PlaylistView(),
        }

        self.layout.register_views(self.views)

    def bind(self, controller):
        self.layout.bind(controller)

    def switch(self, name):
        self.layout.switch_view(name)

    def start(self):
        self.layout.show()
