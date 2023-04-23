from abc import ABCMeta, abstractmethod
from L6.ssh_log_entries.SSHLogPasswordAccepted import SSHLogPasswordAccepted
from L6.ssh_log_entries.SSHLogPasswordDenied import SSHLogPasswordDenied
from L6.ssh_log_entries.SSHLogError import SSHLogError
from L6.ssh_log_entries.SSHLogOther import SSHLogOther
from L6.ssh_log_entries import SSHLogEntry
from L6.type_enum import TypeOfMessage as Msg


# pre declaration
class SSHLogFactory(metaclass=ABCMeta):
    pass


class SSHErrorLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return SSHLogOther(log)


class SSHLogFactory(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create_ssh_entry_obj(self, log):
        pass

    @staticmethod
    def get_log_entry(log_entry):

        factories_dict = {
            Msg.ERROR: SSHErrorLogFactory,
            Msg.PASSWORD_DENIED: SSHPasswordDeniedLogFactory,
            Msg.PASSWORD_ACCEPTED: SSHPasswordAcceptedLogFactory,
            Msg.OTHER: SSHOtherLogFactory
        }

        return factories_dict[SSHLogEntry.get_message_type(log_entry)].create_ssh_entry_obj(log_entry)
