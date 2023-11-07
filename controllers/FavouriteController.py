from PySide6.QtCore import QObject
from view_models.main import ViewModel
from views.main import View
from services.main import Service


class FavouriteController(QObject):
    def __init__(self,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        super().__init__()

        # self._view = view
        self.service = service
        self.view_model = view_model.index
