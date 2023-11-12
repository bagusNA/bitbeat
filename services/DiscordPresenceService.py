from datetime import datetime, timedelta
from dotenv import dotenv_values
from pypresence import Presence
from models.Song import Song


class DiscordPresenceService:
    _CLIENT_ID: str
    current_song: Song

    buttons = [
        {
            'label': 'GitHub',
            'url': 'https://github.com/bagusNA/bitbeat',
        }
    ]

    def __init__(self):
        env = dotenv_values('.env')

        self._CLIENT_ID = env['DISCORD_APP_ID']

        self.RPC = Presence(self._CLIENT_ID)
        self.is_connected = False

        # try:
        #     self.RPC.connect()
        #     self.is_connected = True
        # except ConnectionRefusedError:
        #     pass

        self.reset_status()

    def __del__(self):
        if not self.is_connected:
            return

        self.RPC.close()

    def reset_status(self):
        if not self.is_connected:
            return

        self.RPC.update(
            details="Deciding what song to vibe to",
            buttons=self.buttons
        )

    def set_song(self, song: Song):
        self.current_song = song
        self.update_song()

    def update_song(self):
        if not self.is_connected:
            return

        current_time = datetime.now()
        end_time = current_time + timedelta(seconds=self.current_song.duration)

        btn_data = {
            'label': 'Play',
            'url': self.current_song.url
        }

        if (len(self.buttons) == 2):
            self.buttons[0] = btn_data
        else:
            self.buttons.insert(0, btn_data)

        self.RPC.update(
            details=self.current_song.title,
            state=self.current_song.artist,
            large_image=self.current_song.thumbnail_url,
            large_text=f"{self.current_song.title} - {self.current_song.artist}",
            start=round(current_time.timestamp()),
            # FIXME: Update end time on playback scrobble
            end=round(end_time.timestamp()),
            buttons=self.buttons,
        )
