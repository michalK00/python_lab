from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogError(SSHLogEntry):
    def __init__(self, log: str):
        super().__init__(log, Msg.ERROR)

    def validate(self) -> bool:
        return super().validate()
