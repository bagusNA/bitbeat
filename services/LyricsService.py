from PySide6.QtCore import QObject, QThread, Signal, Slot

from dotenv import dotenv_values
from lyricsgenius import Genius
from lyricsgenius.types import Song


class LyricsWorker(QThread):
    lyricsFetched = Signal(object)

    def __init__(self, service):
        super(LyricsWorker, self).__init__()

        env = dotenv_values('.env')
        self.genius = Genius(env['GENIUS_ACCESS_TOKEN'])
        self.service = service

    def run(self) -> None:
        song: Song | None = self.genius.search_song(self.service._title)

        if song is None:
            self.lyricsFetched.emit(None)
        else:
            self.lyricsFetched.emit(song.lyrics)


class LyricsService(QObject):
    lyricsFetched = Signal(object)

    def __init__(self, service):
        super(LyricsService, self).__init__()

        self._service = service
        self._worker = LyricsWorker(self)
        self._title = ''

        self._worker.lyricsFetched.connect(self.on_lyrics_fetched)

    def search_current_song(self):
        self._title = self._service.audio_player.current_song.title
        self._worker.start()

    def format_lyrics(self, lyrics: str):
        lines = lyrics.splitlines()
        lines.pop(0)  # Removes unnecessary contributor line
        lines.pop(0)  # Removes empty line

        filtered_lines = filter(lambda line: not line.startswith('[') and not line.endswith(']'), lines)
        return filtered_lines


    @Slot(object)
    def on_lyrics_fetched(self, lyrics: str | None):
        if lyrics is None:
            self.lyricsFetched.emit(None)
            return

        lyric_lines = self.format_lyrics(lyrics)

        self.lyricsFetched.emit(lyric_lines)
