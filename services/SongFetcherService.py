import yt_dlp
from models.Song import Song


class SongFetcherService:
    def __init__(self, service, config=None):
        if config is None:
            config = {'format': 'bestaudio'}

        self._service = service
        self._yt_dlp = yt_dlp.YoutubeDL(config)

    def __del__(self):
        self._yt_dlp.close()

    def fetch_song(self, url: str, audio_only=True) -> Song:
        unsanitized_info = self._yt_dlp.extract_info(url, download=False)
        info = self._yt_dlp.sanitize_info(unsanitized_info)

        if (audio_only):
            audio_only_formats = list(filter(self.is_format_audio_only, info['formats']))
            info['formats'] = self.sort_format_by_quality(audio_only_formats)
            info['audio_url'] = info['formats'][0]['url']

        return Song(info)

    # Utilities
    def is_format_audio_only(self, format: dict) -> bool:
        return ('vcodec' in format) and (format['vcodec'] == 'none') and ('acodec' in format) and (format['acodec'] != 'none')

    def sort_format_by_quality(self, formats: list) -> list:
        return sorted(formats, key=lambda format: int(format['quality']), reverse=True)
