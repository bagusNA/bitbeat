from PySide6.QtCore import Qt, QTimer, QPoint
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout


class Toast(QWidget):
    def __init__(self, text=None, duration=3, parent=None):
        super(Toast, self).__init__(parent)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint | Qt.WindowType.SubWindow)

        self._parent = parent
        self._duration = duration
        self._label = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(self._label)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

        if text is not None:
            self.set_text(text)

    def set_text(self, text: str):
        self.show()
        self._label.setText(text)

        width = self._label.fontMetrics().boundingRect(text).width()
        self.setMinimumWidth(width + 50)  # I have no idea why it needs padding like this
        self.update_position()

    def remove_text(self):
        self._label.setText('')

    def clear(self):
        self.remove_text()
        self.hide()

    def update_position(self):
        self.move(self.position())

    def position(self):
        xpos = self._parent.width() - self.width()
        ypos = 0

        return QPoint(xpos, ypos)
