from enum import Enum


class Message(Enum):
    SCREEN_CHANGED = "SCREEN_CHANGED"
    SESSION_RESTARTED = "SESSION_RESTARTED"
    SESSION_STARTED = "SESSION_STARTED"
    SESSION_STOPPED = "SESSION_STOPPED"