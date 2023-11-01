from controllers.IndexController import IndexController
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

        self.index = IndexController(self.view_model, self.view, self.service)

    def start(self):
        self.view.start()
