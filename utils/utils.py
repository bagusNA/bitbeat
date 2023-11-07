from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget


def coalesce(*arg):
    return next((a for a in arg if a is not None), None)


def seconds_to_minutes(seconds: int) -> str:
    minutes = seconds // 60
    left_seconds = seconds % (minutes * 60) if minutes != 0 else seconds

    return f"{str(minutes).rjust(2, '0')}:{str(left_seconds).rjust(2, '0')}"


def remove_all_widgets(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


class Font:
    FONT_FAMILY = 'Nunito'

    @classmethod
    def set_font_size(cls, widget: QWidget, size: int):
        widget.setFont(QFont(cls.FONT_FAMILY, size))
