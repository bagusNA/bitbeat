from __future__ import annotations
from typing import TYPE_CHECKING

from PySide6.QtCore import QObject

from services.main import Service
from view_models.main import ViewModel
from views.main import View

if TYPE_CHECKING:
    from controllers.main import Controller


class SearchController(QObject):
    def __init__(self,
                 controller: Controller,
                 view_model: ViewModel,
                 view: View,
                 service: Service):
        super().__init__()

        self._controller = controller
        self._view = view
        self.service = service
        self.view_model = view_model.index
