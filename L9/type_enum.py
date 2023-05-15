from enum import Enum, auto


class TypeOfMessage(Enum):
    PASSWORD_ACCEPTED: int = auto()
    PASSWORD_DENIED: int = auto()
    ERROR: int = auto()
    OTHER: int = auto()
