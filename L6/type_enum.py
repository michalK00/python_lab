from enum import Enum, auto


class TypeOfMessage(Enum):

    PASSWORD_ACCEPTED = auto()
    PASSWORD_DENIED = auto()
    ERROR = auto()
    OTHER = auto()
