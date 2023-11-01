from view_models.IndexViewModel import IndexViewModel
from services.main import Service


class ViewModel:
    def __init__(self, service: Service):
        self._service = service

        self.index = IndexViewModel(self._service)
