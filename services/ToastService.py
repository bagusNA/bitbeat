from PySide6.QtCore import QObject

from widgets.Toast import Toast


class ToastService(QObject):
    def __init__(self):
        super(ToastService, self).__init__()

        self.toast = None

    def bind(self, toast: Toast):
        self.toast = toast

    def show(self, text: str):
        self.toast.set_text(text)

    def clear(self):
        self.toast.clear()
