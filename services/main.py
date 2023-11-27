from .AudioPlayerService import AudioPlayerService
from .DiscordPresenceService import DiscordPresenceService
from .LibraryService import LibraryService
from .LyricsService import LyricsService
from .SongFetcherService import SongFetcherService
from .CacherService import CacherService


class Service:
    def __init__(self):
        self.song_fetcher = SongFetcherService(self)
        self.audio_player = AudioPlayerService(self)
        self.discord_presence = DiscordPresenceService()
        self.library = LibraryService()
        self.cacher = CacherService()
        self.lyrics = LyricsService(self)
