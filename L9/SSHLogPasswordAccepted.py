from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogPasswordAccepted(SSHLogEntry):
    def __init__(self, log: str):
        super().__init__(log, Msg.PASSWORD_ACCEPTED)

    def validate(self) -> bool:
        return super().validate()
