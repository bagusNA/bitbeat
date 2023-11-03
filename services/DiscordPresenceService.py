from datetime import datetime, timedelta
from dotenv import dotenv_values
from pypresence import Presence
from models.Song import Song


class DiscordPresenceService:
    _CLIENT_ID: str

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
        self.RPC.connect()

        self.RPC.update(
            details="Deciding what song to vibe to",
            buttons=self.buttons
        )

    def __del__(self):
        self.RPC.close()

    def update_song(self, song: Song):
        current_time = datetime.now()
        end_time = current_time + timedelta(seconds=song.duration)

        btn_data = {
            'label': 'Play',
            'url': song.url
        }

        if (len(self.buttons) == 2):
            self.buttons[0] = btn_data
        else:
            self.buttons.insert(0, btn_data)

        self.RPC.update(
            details=song.title,
            state=song.artist,
            large_image=song.thumbnail_url,
            large_text=f"{song.title} - {song.artist}",
            start=round(current_time.timestamp()),
            end=round(end_time.timestamp()),
            buttons=self.buttons,
        )
