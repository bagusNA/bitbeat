from .AudioPlayerService import AudioPlayerService
from .DiscordPresenceService import DiscordPresenceService
from .LibraryService import LibraryService
from .SongFetcherService import SongFetcherService


class Service:
    def __init__(self):
        self.song_fetcher = SongFetcherService(self)
        self.audio_player = AudioPlayerService(self)
        self.discord_presence = DiscordPresenceService()
        self.library = LibraryService()
