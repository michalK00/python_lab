from abc import ABCMeta, abstractmethod
from SSHLogEntry import SSHLogEntry
from SSHLogPasswordAccepted import SSHLogPasswordAccepted
from SSHLogPasswordDenied import SSHLogPasswordDenied
from SSHLogError import SSHLogError
from SSHLogOther import SSHLogOther
from SSHLogEntry import get_message_type
from type_enum import TypeOfMessage as Msg
from typing import Type, Dict, Any, TypeVar

T = TypeVar('T', bound='SSHLogFactory')


class SSHLogFactory(metaclass=ABCMeta):
    pass


class SSHErrorLogFactory(SSHLogFactory):
    @classmethod
    def create_ssh_entry_obj(cls: Type[T], log: str) -> SSHLogError:
        return SSHLogError(log)


class SSHPasswordAcceptedLogFactory(SSHLogFactory):
    @classmethod
    def create_ssh_entry_obj(cls: Type[T], log: str) -> SSHLogPasswordAccepted:
        return SSHLogPasswordAccepted(log)


class SSHPasswordDeniedLogFactory(SSHLogFactory):
    @classmethod
    def create_ssh_entry_obj(cls: Type[T], log: str) -> SSHLogPasswordDenied:
        return SSHLogPasswordDenied(log)


class SSHOtherLogFactory(SSHLogFactory):
    @classmethod
    def create_ssh_entry_obj(cls: Type[T], log: str) -> SSHLogOther:
        return SSHLogOther(log)


class SSHLogFactory(metaclass=ABCMeta):  # type: ignore
    @classmethod
    @abstractmethod
    def create_ssh_entry_obj(cls: Type[T], log: str) -> SSHLogEntry:
        pass

    @classmethod
    def get_log_entry(cls: Type[T], log_entry: str) -> Any:
        factory: Dict[Msg, Type[SSHLogFactory]] = {
            Msg.ERROR: SSHErrorLogFactory,
            Msg.PASSWORD_DENIED: SSHPasswordDeniedLogFactory,
            Msg.PASSWORD_ACCEPTED: SSHPasswordAcceptedLogFactory,
            Msg.OTHER: SSHOtherLogFactory
        }

        res = factory[get_message_type(log_entry)]

        if not isinstance(res, SSHLogFactory):
            return None
        return res.create_ssh_entry_obj(log_entry)
