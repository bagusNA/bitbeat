import time

from PySide6.QtCore import Signal, QThread, Slot
from PySide6.QtGui import QMouseEvent, QPaintEvent, QPainter
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStyleOption, QStyle, QGraphicsOpacityEffect

from utils.utils import Font
from models.Song import Song


class CheckHoverThread(QThread):
    mouse_enter = Signal()
    mouse_leave = Signal()
    mouse_hovering = Signal(bool)

    def __init__(self, parent: QWidget):
        super(CheckHoverThread, self).__init__()
        self.parent = parent
        self.is_hovering = False

    def run(self) -> None:
        while True:
            if self.parent.underMouse() and not self.is_hovering:
                self.mouse_enter.emit()
                self.is_hovering = True
            elif not self.parent.underMouse() and self.is_hovering:
                self.mouse_leave.emit()
                self.is_hovering = False
            elif self.is_hovering:
                self.mouse_hovering.emit(self.mouse_hovering)

            time.sleep(0.1)


class QueueListItem(QWidget):
    FADED_OPACITY = 0.75
    NORMAL_OPACITY = 1.0

    clicked = Signal()

    def __init__(self, song: Song, focused=False, parent=None, *args, **kwargs):
        super(QueueListItem, self).__init__(parent=parent, *args, **kwargs)

        self.thread = CheckHoverThread(self)
        self.thread.mouse_enter.connect(self.on_mouse_enter)
        self.thread.mouse_leave.connect(self.on_mouse_leave)
        self.thread.start()

        self.effect = None
        self._focused = focused

        self.container_layout = QVBoxLayout()
        self.title_label = QLabel(song.title)
        self.artist_label = QLabel(song.artist)

        Font.set_font_size(self.title_label, 11)
        Font.set_font_size(self.artist_label, 7)

        self.container_layout.addWidget(self.title_label)
        self.container_layout.addWidget(self.artist_label)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.container_layout)

        self.change_opacity(self.NORMAL_OPACITY if self.focused else self.FADED_OPACITY)

    @property
    def focused(self):
        return self._focused

    @focused.setter
    def focused(self, value: bool):
        self._focused = value

    @Slot()
    def on_mouse_enter(self):
        self.change_opacity(self.NORMAL_OPACITY)

    @Slot()
    def on_mouse_leave(self):
        self.change_opacity(self.NORMAL_OPACITY if self.focused else self.FADED_OPACITY)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.setProperty("pressed", True)
        self.style().polish(self)
        self.style().unpolish(self)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.setProperty("pressed", False)
        self.style().polish(self)
        self.style().unpolish(self)

        self.clicked.emit()

    def paintEvent(self, event: QPaintEvent) -> None:
        super(QueueListItem, self).paintEvent(event)

        opt = QStyleOption()
        opt.initFrom(self)

        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

    def change_opacity(self, opacity: float):
        self.effect = QGraphicsOpacityEffect(self)
        self.effect.setOpacity(opacity)
        self.setGraphicsEffect(self.effect)
