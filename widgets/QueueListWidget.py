from PySide6.QtWidgets import QPushButton


class QueueListWidget(QPushButton):
    def __init__(self, *args, **kwargs):
        super(QueueListWidget, self).__init__(*args, **kwargs)

        self.setFixedHeight(48)
        self.setStyleSheet("text-align: left;")
