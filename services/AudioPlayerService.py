# import mpv
from PySide6.QtCore import QObject, Signal
from models.Song import Song
from utils.utils import coalesce


class AudioPlayerService(QObject):
    playback_status_changed = Signal(bool)
    current_song_changed = Signal(Song)
    queue_changed = Signal(list)

    def __init__(self, service):
        super().__init__()
        # This in-function 'import mpv' avoids https://github.com/mpv-player/mpv/issues/7102
        # See also https://www.reddit.com/r/programminghorror/comments/dowp0x/comment/f5qyzxj
        import mpv
        self._player = mpv.MPV(video=False, script_opts='keep-open=yes')

        self._service = service
        self._song_fetcher = self._service.song_fetcher
        self._events = []

        self.queue: list[Song] = []
        self.currently_playing_index: int | None = None
        self.is_currently_playing = False

        @self._player.property_observer('eof-reached')
        def on_song_change(property_name, has_reached_eof):
            print(has_reached_eof)
            if (has_reached_eof is True):
                self.next()

    @property
    def current_song(self):
        return self.queue[self.currently_playing_index]

    def on_song_change(self, callback):
        self._events.append(callback)

    def call_song_change_events(self):
        for callback in self._events:
            callback()

    def on_song_ends(self, callback):
        pass

    def add_song(self, url: str) -> None:
        song = self._song_fetcher.fetch_song(url)
        self.queue.append(song)

        if self.currently_playing_index is None:
            self.currently_playing_index = 0
            self.current_song_changed.emit(song)

        self.queue_changed.emit(self.queue)

    def play(self, index: int | None = None) -> None:
        current_song = self.queue[coalesce(index, self.currently_playing_index)]
        self._player.play(current_song.audio_url)
        self.is_currently_playing = True
        self.currently_playing_index = coalesce(index, self.currently_playing_index)

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
        next_index = self.currently_playing_index + 1 if len(self.queue) - 1 is not self.currently_playing_index else 0
        self.play(next_index)

    def previous(self) -> None:
        previous_index = self.currently_playing_index - 1 if self.currently_playing_index != 0 else len(self.queue) - 1
        self.play(previous_index)
