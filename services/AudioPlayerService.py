# import mpv
from PySide6.QtCore import QObject, QThread, Signal
from models.Song import Song
from utils.utils import coalesce


class AudioPlayerService(QObject):
    fetch_song_signal = Signal(str)
    playback_status_changed = Signal(bool)
    current_song_changed = Signal(Song)
    queue_changed = Signal(list)

    playback_position_changed = Signal(int)
    playback_percent_changed = Signal(int)
    playback_volume_changed = Signal(int)
    playback_muted_changed = Signal(bool)

    def __init__(self, service):
        super().__init__()
        # This in-function 'import mpv' avoids https://github.com/mpv-player/mpv/issues/7102
        # See also https://www.reddit.com/r/programminghorror/comments/dowp0x/comment/f5qyzxj
        import mpv
        self._player = mpv.MPV(
            video=False,
            keep_open=True,
        )

        self._service = service
        self._song_fetcher: QObject = self._service.song_fetcher
        self._events = []

        self._bind_threads()

        self.queue: list[Song] = []
        self.currently_playing_index: int | None = None
        self.is_currently_playing = False

        self._playback_position = None
        self._playback_percent = None
        self._playback_volume = None
        self._playback_muted = None

        @self._player.property_observer('time-pos')
        def on_playback_position_change(_, value: float):
            if (value is None):
                return

            seconds = round(value)
            if (seconds == self.playback_position):
                return

            self.playback_position = seconds

        @self._player.property_observer('percent-pos')
        def on_playback_position_change(_, value: float):
            if (value is None):
                return

            percent = round(value)
            if (percent == self.playback_percent):
                return

            self.playback_percent = percent

        @self._player.property_observer('eof-reached')
        def on_song_end(_, value):
            if (value is not True):
                return

            self.next()

    def __del__(self):
        self.thread.quit()
        self.thread.wait()

    def _bind_threads(self):
        self.thread = QThread()
        self._song_fetcher.moveToThread(self.thread)

        self.fetch_song_signal.connect(self._song_fetcher.fetch_song)
        self._song_fetcher.song_fetched.connect(self.add_song)

        self.thread.finished.connect(self.deleteLater)
        self.thread.start()


    @property
    def current_song(self):
        return self.queue[self.currently_playing_index]

    @property
    def playback_position(self):
        return self._playback_position

    @playback_position.setter
    def playback_position(self, value):
        self._playback_position = value
        self.playback_position_changed.emit(value)

    @property
    def playback_percent(self):
        return self._playback_percent

    @playback_percent.setter
    def playback_percent(self, value):
        self._playback_percent = value
        self.playback_percent_changed.emit(value)

    @property
    def playback_volume(self):
        return self._playback_volume

    @playback_volume.setter
    def playback_volume(self, value):
        self._playback_volume = value
        self._player.volume = value
        self.playback_volume_changed.emit(value)

    @property
    def playback_muted(self):
        return self._playback_muted

    @playback_muted.setter
    def playback_muted(self, value: bool) -> None:
        self._playback_muted = value
        self._player.mute = value
        self.playback_muted_changed.emit(value)

    def search_song(self, url: str) -> None:
        self.fetch_song_signal.emit(url)

    def add_song(self, song: Song):
        self.queue.append(song)

        if self.currently_playing_index is None:
            self.currently_playing_index = 0
            self.current_song_changed.emit(song)

        self.queue_changed.emit(self.queue)

    def play(self, index: int | None = None) -> None:
        if (len(self.queue) == 0):
            return

        current_song = self.queue[coalesce(index, self.currently_playing_index)]
        self._player.play(current_song.audio_url)
        self.is_currently_playing = True
        self.currently_playing_index = coalesce(index, self.currently_playing_index)

        self._service.discord_presence.set_song(current_song)
        self.current_song_changed.emit(current_song)
        self.playback_status_changed.emit(self.is_currently_playing)

    def resume(self) -> None:
        self._player.pause = False
        self.is_currently_playing = True
        self.playback_status_changed.emit(self.is_currently_playing)

    def pause(self) -> None:
        self._player.pause = True
        self.is_currently_playing = False
        self.playback_status_changed.emit(self.is_currently_playing)

    def toggle(self) -> None:
        if (self._player.pause == False and self.is_currently_playing == False):
            return self.play()

        self._player.pause = not self._player.pause
        self.is_currently_playing = not self._player.pause
        self.playback_status_changed.emit(self.is_currently_playing)

    def next(self) -> None:
        if (len(self.queue) == 0):
            return

        next_index = self.currently_playing_index + 1 if len(self.queue) - 1 != self.currently_playing_index else 0
        self.play(next_index)

    def previous(self) -> None:
        if (len(self.queue) == 0):
            return

        previous_index = self.currently_playing_index - 1 if self.currently_playing_index != 0 else len(self.queue) - 1
        self.play(previous_index)

    def move_playback_to(self, percent):
        self._player.percent_pos = percent
        self.playback_percent = percent
