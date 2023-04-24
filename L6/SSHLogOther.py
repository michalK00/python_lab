from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogOther(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log, Msg.OTHER)

    def validate(self):
        return True
