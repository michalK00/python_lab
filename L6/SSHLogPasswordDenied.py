import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogPasswordDenied(SSHLogEntry):
    def __int__(self, log):
        super.__init__(self, log, Msg.PASSWORD_DENIED)

    def validate(self):
        return super.validate(self)
