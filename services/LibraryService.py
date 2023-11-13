from PySide6.QtCore import QObject, Signal

from models.Playlist import Playlist
from models.Song import Song


class LibraryService(QObject):
    favourited_songs_changed = Signal(object)

    def __init__(self):
        super(LibraryService, self).__init__()

    def get_all_songs(self) -> list[Song]:
        return list(Song.select().execute())

    def get_recent_songs(self, page=1, limit=4) -> list[Song]:
        songs = Song.select()\
            .order_by(Song.last_played_at.desc())\
            .paginate(page, limit)\
            .execute()

        return list(songs)

    def get_favourited_songs(self, page=1, limit=25) -> list[Song]:
        songs = Song.select()\
            .where(Song.is_favourite == True) \
            .order_by(Song.favourited_at.desc())\
            .paginate(page, limit)\
            .execute()

        return list(songs)

    def toggle_song_favourite(self, song: Song) -> None:
        song.toggle_favourite()
        self.favourited_songs_changed.emit(song)

    def get_all_playlist(self) -> list[Playlist]:
        playlists = Playlist.select().execute()

        return list(playlists)

    def get_recent_playlist(self, page=1, limit=4) -> list[Playlist]:
        playlists = Playlist.select() \
            .order_by(Playlist.imported_at.desc()) \
            .paginate(page, limit) \
            .execute()

        return list(playlists)
