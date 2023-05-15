from abc import ABCMeta
from SSHLogEntry import SSHLogEntry
from SSHLogPasswordAccepted import SSHLogPasswordAccepted
from SSHLogPasswordDenied import SSHLogPasswordDenied
from SSHLogError import SSHLogError
from SSHLogOther import SSHLogOther
from SSHLogEntry import get_message_type
from type_enum import TypeOfMessage as Msg
from typing import Type, Dict


# improved factory
class SSHLogFactory(metaclass=ABCMeta):
    @staticmethod
    def get_log_entry(log_entry: str) -> SSHLogEntry:
        factory: Dict[
            Msg, Type[SSHLogError | SSHLogPasswordAccepted | SSHLogPasswordDenied]
        ] = {
            Msg.ERROR: SSHLogError,
            Msg.PASSWORD_DENIED: SSHLogPasswordDenied,
            Msg.PASSWORD_ACCEPTED: SSHLogPasswordAccepted,
        }

        # default value is SSHLogOther if no value is found in dict
        res = factory.get(get_message_type(log_entry), SSHLogOther)

        return res(log=log_entry)
