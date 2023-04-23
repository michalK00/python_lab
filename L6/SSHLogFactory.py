from abc import ABCMeta, abstractmethod
import SSHLogError as error
import SSHLogOther as other
import SSHLogPasswordAccepted as accepted
import SSHLogPasswordDenied as denied
import SSHLogEntry


class SSHLogFactory:

    @abstractmethod
    def create_ssh_entry_obj(log):
        pass


class SSHErrorLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log) -> SSHLogEntry:
        return error.SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log) -> SSHLogEntry:
        return accepted.SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log) -> SSHLogEntry:
        return denied.SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    @staticmethod
    def create_ssh_entry_obj(log) -> SSHLogEntry:
        return other.SSHLogOther(log)
