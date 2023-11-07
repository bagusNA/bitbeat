from PySide6.QtCore import QObject, Signal

from models.Song import Song


class LibraryService(QObject):
    favourited_songs_changed = Signal(object)

    def __init__(self):
        super(LibraryService, self).__init__()

    def get_all_songs(self):
        return list(Song.select().execute())

    def get_favourited_songs(self, page=1, limit=25):
        songs = Song.select()\
            .where(Song.is_favourite == True)\
            .paginate(page, limit)\
            .order_by(Song.favourited_at.desc())\
            .execute()
        return list(songs)

    def toggle_song_favourite(self, song: Song):
        song.toggle_favourite()
        self.favourited_songs_changed.emit(song)