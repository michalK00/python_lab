from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogError(SSHLogEntry):
    def __int__(self, log):
        super.__init__(self, log, Msg.ERROR)

    def validate(self):
        return super.validate(self)
