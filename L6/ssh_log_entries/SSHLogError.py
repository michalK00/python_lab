from ssh_log_entries.SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogError(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log, Msg.ERROR)

    def validate(self):
        return super().validate()
