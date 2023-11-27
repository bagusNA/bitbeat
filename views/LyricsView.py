from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget, QLabel

from utils.utils import remove_all_widgets
from ui.ui_lyrics_view import Ui_lyrics_view as Ui


class LyricsView(QWidget):
    def __init__(self):
        super(LyricsView, self).__init__()

        self._controller = None
        self._loaded_current_song_lyrics = False
        self._is_view_focused = False

        self._loading_widget = None

        self.ui = Ui()
        self.ui.setupUi(self)

    def bind(self, controller):
        self._controller = controller.lyrics
        self._controller.service.lyrics.lyricsFetched.connect(self.build_lyrics)
        self._controller.service.audio_player.current_song_changed.connect(self.on_song_change)

    def on_show(self):
        self._is_view_focused = True
        if self._loaded_current_song_lyrics:
            return

        self.clear_lyrics()
        self.show_loading()
        self._controller.service.lyrics.search_current_song()

    def on_leave(self):
        self._is_view_focused = False

    def on_song_change(self):
        self._loaded_current_song_lyrics = False
        self.clear_lyrics()

        if self._is_view_focused is False:
            return

        self._controller.service.lyrics.search_current_song()

    @Slot(object)
    def build_lyrics(self, lyrics: list[str] | None):
        self._loaded_current_song_lyrics = True
        self.hide_loading()

        if lyrics is None:
            not_found_label = QLabel("Lyrics not found")

            self.ui.lyrics_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.lyrics_container.addWidget(not_found_label)
        else:
            self.ui.lyrics_container.setAlignment(Qt.AlignmentFlag.AlignLeft)

            for line in lyrics:
                line_widget = QLabel(line)
                self.ui.lyrics_container.addWidget(line_widget)

    def clear_lyrics(self):
        remove_all_widgets(self.ui.lyrics_container)

    def show_loading(self):
        self.ui.lyrics_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._loading_widget = QLabel("Loading...")
        self.ui.lyrics_container.addWidget(self._loading_widget)
        self._loading_widget.show()

    def hide_loading(self):
        self.ui.lyrics_container.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self._loading_widget.hide()
