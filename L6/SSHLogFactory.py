from abc import ABCMeta, abstractmethod
import SSHLogError as Error
import SSHLogOther as Other
import SSHLogPasswordAccepted as Accepted
import SSHLogPasswordDenied as Denied
import SSHLogEntry
from type_enum import TypeOfMessage as Msg

# pre declaration
class SSHLogFactory(metaclass=ABCMeta):
    pass


class SSHErrorLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return Error.SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return Accepted.SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return Denied.SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return Other.SSHLogOther(log)


class SSHLogFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_ssh_entry_obj(self, log):
        pass

    @staticmethod
    def get_log_entry(log_entry):

        factories_dict = {
            Msg.ERROR: SSHErrorLogFactory(),
            Msg.PASSWORD_DENIED: SSHPasswordDeniedLogFactory(),
            Msg.PASSWORD_ACCEPTED: SSHPasswordAcceptedLogFactory(),
            Msg.OTHER: SSHOtherLogFactory()
        }

        return factories_dict[SSHLogEntry.get_message_type(log_entry)].create_ssh_entry_obj(log_entry)
