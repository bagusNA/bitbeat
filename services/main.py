from .AudioPlayerService import AudioPlayerService
from .SongFetcherService import SongFetcherService


class Service:
    def __init__(self):
        self.song_fetcher = SongFetcherService(self)
        self.audio_player = AudioPlayerService(self)
