from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogPasswordAccepted(SSHLogEntry):
    def __int__(self, log):
        super.__init__(self, log, Msg.PASSWORD_ACCEPTED)

    def validate(self):
        return super.validate(self)
