from enum import Enum, auto


# redundant over logging.TYPE_OF_LOG but improves readability!
class TypeOfMessage(Enum):

    PASSWORD_ACCEPTED = auto()
    PASSWORD_DENIED = auto()
    ERROR = auto()
    OTHER = auto()
