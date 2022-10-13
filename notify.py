import dotenv
import os

from discord_message import DiscordMessage
from gmail_message import GmailMessage
from distutils.util import strtobool


class Notify:
    def __init__(self):
        dotenv.load_dotenv()
        self.gmail_enabled = bool(strtobool(os.getenv("GMAIL_ENABLED")))
        self.discord_enabled = bool(strtobool(os.getenv("DISCORD_ENABLED")))
        self.gmail = None
        self.discord = None
        if self.gmail_enabled:
            self.gmail = GmailMessage()
        if self.discord_enabled:
            self.discord = DiscordMessage()

    def notify(self, message):
        if self.gmail_enabled:
            self.gmail.send(message)
        if self.discord_enabled:
            self.discord.send(message)
