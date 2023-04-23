from abc import ABCMeta, abstractmethod
from L6.ssh_log_entries import SSHLogEntry, SSHLogOther as Other, SSHLogPasswordDenied as Denied, \
    SSHLogPasswordAccepted as Accepted, SSHLogError as Error
from type_enum import TypeOfMessage as Msg


# pre declaration
class SSHLogFactory(metaclass=ABCMeta):
    pass


class SSHErrorLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return Error.SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return Accepted.SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return Denied.SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log):
        return Other.SSHLogOther(log)


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
