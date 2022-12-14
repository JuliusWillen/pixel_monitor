from discord import SyncWebhook
import dotenv
import os
from message import Message


class DiscordMessage:
    def __init__(self):
        dotenv.load_dotenv()
        self.messages = {Message.SCREEN_CHANGED: "Screen changed",
                         Message.SESSION_RESTARTED: "Session restarted",
                         Message.SESSION_STARTED: "Session started",
                         Message.SESSION_STOPPED: "Session stopped"}
        self.id = "<@" + os.getenv("DISCORD_ID") + ">"

        self.webhook = SyncWebhook.from_url(os.getenv("DISCORD_WEBHOOK_URL"))

    def send(self, message):
        try:
            msg = self.messages[message]
            self.webhook.send(self.id + ": " + msg)
        except:
            print("DiscordMessage: something went wrong")
