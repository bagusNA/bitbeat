from PySide6.QtWidgets import QPushButton


class QueueListItem(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QueueListItem, self).__init__(*args, **kwargs)

        self.setFixedHeight(48)
        self.setStyleSheet("text-align: left;")
