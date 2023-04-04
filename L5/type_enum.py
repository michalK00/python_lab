from enum import Enum, auto


class TypeOfMessage(Enum):
    LOGIN_OR_DISCONNECT_SUCCESS = auto()
    LOGIN_FAILURE = auto()
    ERROR = auto()
    HACK_ATTEMPT = auto()
