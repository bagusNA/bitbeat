import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPaintEvent, QPainter, Qt
from PySide6.QtWidgets import QLabel, QWidget


class HoverThread(QThread):
    on_enter = Signal()
    on_exit = Signal()
    on_hover = Signal(bool)

    def __init__(self, parent: QWidget):
        super(HoverThread, self).__init__()

        self.parent = parent
        self.is_hovering = False

    def run(self) -> None:
        while True:
            try:
                is_under_mouse = self.parent.underMouse()
            except RuntimeError:
                is_under_mouse = False

            if is_under_mouse and self.is_hovering is False:
                self.is_hovering = True
                self.on_enter.emit()
            elif not is_under_mouse and self.is_hovering is True:
                self.is_hovering = False
                self.on_exit.emit()
            elif self.is_hovering:
                self.on_hover.emit(True)

            time.sleep(0.05)


class MarqueeLabel(QLabel):
    def __init__(self, hover_parent=None, *args, **kwargs):
        super(MarqueeLabel, self).__init__(*args, **kwargs)

        self._hover_parent = hover_parent if hover_parent is not None else self

        self.painter = None
        self.is_hovered = False

        self.x_pos = 0
        self.rewind_stop_time = 0
        self.rewind_delay = 45

        self.thread = HoverThread(self._hover_parent)
        self.thread.on_enter.connect(self.on_mouse_enter)
        self.thread.on_exit.connect(self.on_mouse_exit)
        self.thread.on_hover.connect(self.repaint)

        self.thread.start()

    def on_mouse_enter(self):
        self.is_hovered = True
        self.rewind_stop_time = 0

        self.repaint()

    def on_mouse_exit(self):
        self.is_hovered = False
        self.x_pos = 0

        self.repaint()

    def paintEvent(self, e: QPaintEvent) -> None:
        self.painter = QPainter(self)

        max_font_width = self.fontMetrics().horizontalAdvance(self.text())
        max_travel = max_font_width - self.width()

        if self.is_hovered:
            if self.x_pos < -max_travel:
                self.rewind_stop_time += 1  # Wait for delay
            else:
                self.x_pos -= 1

            if self.rewind_stop_time > self.rewind_delay:
                self.x_pos = 0
                self.rewind_stop_time = 0

        self.painter.setFont(self.font())
        self.painter.setPen(Qt.GlobalColor.white)
        self.painter.drawText(self.x_pos, self.height() - 4, self.text())

        self.painter.end()
