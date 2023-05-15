import re
from datetime import datetime
from type_enum import TypeOfMessage as Msg
from ipaddress import IPv4Address
from abc import ABCMeta, abstractmethod
from typing import Match, List


def get_message_type(row: str) -> Msg:
    pass_acc: str = "Accepted password"
    pass_den: str = "Failed password"
    error: str = "error:"

    if re.search(pass_acc, row):
        return Msg.PASSWORD_ACCEPTED
    elif re.search(pass_den, row):
        return Msg.PASSWORD_DENIED
    elif re.search(error, row):
        return Msg.ERROR
    else:
        return Msg.OTHER


def get_date_if_valid_else_now(row: str) -> datetime:
    date_regex: str = r"([A-z]{3})\s+(0?[1-9]|[12][0-9]|3[01]) (?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)"
    match: Match[str] | None = re.search(date_regex, row)
    if not match:
        return datetime.now()

    month: str = match.group(1)
    day: str = match.group(2)
    hour: str = match.group(3)
    minute: str = match.group(4)
    second: str = match.group(5)

    date_string: str = f"{day} {month} {datetime.now().year} {hour}:{minute}:{second}"
    date_obj: datetime = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
    return date_obj


def get_pid(row: str) -> int | None:
    pid_regex: str = r"sshd\[(\d+)\]"
    match: Match[str] | None = re.search(pid_regex, row)
    if match:
        return int(match.group(1))
    else:
        return None


def get_user_from_log(row: str) -> str | None:
    user_regex: str = r"user (\w+)"
    match: Match[str] | None = re.search(user_regex, row)
    if match:
        return match.group(1)
    else:
        return None


def get_ipv4s_from_log(row: str) -> IPv4Address | None:
    ip_regex: str = r"(?:\d{1,3}\.){3}\d{1,3}"
    match: List[str] = re.findall(ip_regex, row)
    if match:
        return IPv4Address(match[0])
    else:
        return None


class SSHLogEntry(metaclass=ABCMeta):
    def __init__(self, log: str, message_type: Msg):
        self.date: datetime = get_date_if_valid_else_now(log)
        self.user: str | None = get_user_from_log(log)
        self.ip_v4: IPv4Address | None = get_ipv4s_from_log(log)
        self.message_type: Msg = message_type
        self.pid: int | None = get_pid(log)
        self._raw_log: str = log

    def __str__(self) -> str:
        return (
            "PID: "
            + str(self.pid)
            + " date: "
            + str(self.date)
            + (f" user: {str(self.user)}" if self.user is not None else "")
            + " ip_v4: "
            + str(self.ip_v4)
            + " message_type: "
            + str(self.message_type)
        )

    @abstractmethod
    def validate(self) -> bool:
        return (
            self.date == get_date_if_valid_else_now(self._raw_log)
            and self.user == get_user_from_log(self._raw_log)
            and self.ip_v4 == get_ipv4s_from_log(self._raw_log)
            and self.message_type == get_message_type(self._raw_log)
            and self.pid == get_pid(self._raw_log)
        )

    def get_ip(self) -> IPv4Address | None:
        return self.ip_v4

    @property
    def has_ip(self) -> bool:
        return self.ip_v4 is not None

    def __repr__(self) -> str:
        return f"{self.__class__}, {self.__dict__}"

    # type hinting to access the _raw_log
    def __lt__(self, other: "SSHLogEntry") -> bool:
        # if self.pid < other.pid:
        #     return True
        # if self.pid > other.pid:
        #     return False
        # if self.date < other.date:
        #     return True
        # if self.date > other.date:
        #     return False
        # if self._raw_log < other._raw_log:
        #     return True
        # return False
        # Tuple comparison, does the same as this code (comparing element by element), but is much more concise

        return (self.pid, self.date, self._raw_log) < (
            other.pid,
            other.date,
            other._raw_log,
        )

    def __gt__(self, other: "SSHLogEntry") -> bool:
        return (self.pid, self.date, self._raw_log) > (
            other.pid,
            other.date,
            other._raw_log,
        )

    # ignoring mypy type, as other has to be SSHLogFactory to be comparable
    def __eq__(self, other: "SSHLogEntry") -> bool:  # type: ignore
        return not (self.__lt__(other) or self.__gt__(other))
