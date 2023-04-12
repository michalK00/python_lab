from enum import Enum, auto


# redundant over logging.TYPE_OF_LOG but improves readability!
class TypeOfMessage(Enum):

    LOGIN_SUCCESSFUL = auto()
    LOGIN_FAILURE = auto()
    CONNECTION_CLOSED = auto()
    WRONG_USER = auto()
    WRONG_PASSWORD = auto()
    BREAK_IN_ATTEMPT = auto()
    OTHER = auto()
