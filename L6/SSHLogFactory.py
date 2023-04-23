from abc import ABCMeta, abstractmethod
import SSHLogError
import SSHLogOther
import SSHLogPasswordAccepted
import SSHLogPasswordDenied
import SSHLogEntry


class SSHLogFactory:

    @abstractmethod
    def create_ssh_entry_obj(self, log):
        pass


class SSHErrorLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    def create_ssh_entry_obj(self, log) -> SSHLogEntry:
        return SSHLogOther(log)
