from abc import ABCMeta, abstractmethod
from SSHLogPasswordAccepted import SSHLogPasswordAccepted
from SSHLogPasswordDenied import SSHLogPasswordDenied
from SSHLogError import SSHLogError
from SSHLogOther import SSHLogOther
from SSHLogEntry import get_message_type, SSHLogEntry
from type_enum import TypeOfMessage as Msg


# pre declaration
class SSHLogFactory(metaclass=ABCMeta):
    pass


class SSHErrorLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log: str) -> SSHLogError:
        return SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log: str) -> SSHLogPasswordAccepted:
        return SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log: str) -> SSHLogPasswordDenied:
        return SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log: str) -> SSHLogOther:
        return SSHLogOther(log)


class SSHLogFactory(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create_ssh_entry_obj(self, log: str):
        pass

    @staticmethod
    def get_log_entry(log_entry: str) -> SSHLogEntry:

        factories_dict = {
            Msg.ERROR: SSHErrorLogFactory,
            Msg.PASSWORD_DENIED: SSHPasswordDeniedLogFactory,
            Msg.PASSWORD_ACCEPTED: SSHPasswordAcceptedLogFactory,
            Msg.OTHER: SSHOtherLogFactory
        }

        return factories_dict[get_message_type(log_entry)]\
            .create_ssh_entry_obj(log_entry)
