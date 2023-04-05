from enum import Enum, auto


# redundant over logging.TYPE_OF_LOG but improves readability!
class TypeOfMessage(Enum):
    LOGIN_OR_DISCONNECT_SUCCESS = auto()
    LOGIN_FAILURE = auto()
    ERROR = auto()
    HACK_ATTEMPT = auto()
