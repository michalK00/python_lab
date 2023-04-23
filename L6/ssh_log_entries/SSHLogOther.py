from L6.ssh_log_entries.SSHLogEntry import SSHLogEntry
from L6.type_enum import TypeOfMessage as Msg


class SSHLogOther(SSHLogEntry):
    def __init__(self, log):
        super().__init__(log, Msg.OTHER)

    def validate(self):
        return True
