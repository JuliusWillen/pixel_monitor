
import dotenv
import os
import yagmail


class GmailMessage:
    def __init__(self):
        dotenv.load_dotenv()
        self.messages = {"SCREEN_CHANGED": ("Screen changed", ["The screen has changed", "ss.png"]),
                         "SESSION_RESTARTED": ("Session restarted", ["The session has restarted", "ss.png"]),
                         "SESSION_STARTED": ("Session started", "The session has started"),
                         "SESSION_STOPPED": ("Session stopped", "The session has stopped")}
        self.yag = yagmail.SMTP(os.getenv("GMAIL_USERNAME"),
                                os.getenv("GMAIL_APP_PASSWORD"))
        self.to_mail = os.getenv("TO_MAIL")

    def send(self, message):
        try:
            msg = self.messages[message]
            if isinstance(msg, tuple):
                self.yag.send(self.to_mail, msg[0], msg[1])
        except:
            print("GmailMessage: something went wrong")
