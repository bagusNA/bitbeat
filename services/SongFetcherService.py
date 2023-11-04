import yt_dlp
from peewee import DoesNotExist
from PySide6.QtCore import QObject, Signal
from models.Song import Song


class SongFetcherService(QObject):
    song_fetched = Signal(object)

    def __init__(self, service, config=None):
        super().__init__()

        if config is None:
            config = {
                'format': 'bestaudio',
                'noplaylist': True,
            }

        self._service = service
        self._yt_dlp = yt_dlp.YoutubeDL(config)

    def __del__(self):
        self._yt_dlp.close()

    def fetch_song(self, url: str, audio_only=True) -> None:
        unsanitized_info = self._yt_dlp.extract_info(url, download=False)
        info = self._yt_dlp.sanitize_info(unsanitized_info)

        songs: list[Song] = []
        unformatted_songs = info['entries'] if (info['_type'] == 'playlist') else [info]

        for song_info in unformatted_songs:
            if (audio_only):
                audio_only_formats = list(filter(self.is_format_audio_only, song_info['formats']))
                song_info['formats'] = self.sort_format_by_quality(audio_only_formats)
                song_info['audio_url'] = song_info['formats'][0]['url']

            is_new_song = False
            try:
                song = Song.get_by_id(song_info['id'])
            except DoesNotExist:
                song = Song()
                is_new_song = True

            song.load(song_info)

            if is_new_song:
                song.save_force()

            songs.append(song)

        self.song_fetched.emit(songs)

    # Utilities
    def is_format_audio_only(self, format: dict) -> bool:
        return ('vcodec' in format) and (format['vcodec'] == 'none') and ('acodec' in format) and (format['acodec'] != 'none')

    def sort_format_by_quality(self, formats: list) -> list:
        return sorted(formats, key=lambda format: int(format['quality']), reverse=True)
