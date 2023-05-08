import re
from datetime import datetime
from type_enum import TypeOfMessage as Msg
import ipaddress
from abc import ABCMeta, abstractmethod


def get_message_type(row):
    pass_acc = "Accepted password"
    pass_den = "Failed password"
    error = "error:"

    if re.search(pass_acc, row):
        return Msg.PASSWORD_ACCEPTED
    elif re.search(pass_den, row):
        return Msg.PASSWORD_DENIED
    elif re.search(error, row):
        return Msg.ERROR
    else:
        return Msg.OTHER


def get_date(row):
    date_regex = r'([A-z]{3})\s+(0?[1-9]|[12][0-9]|3[01]) (?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)'
    match = re.search(date_regex, row)
    if match:
        month = match.group(1)
        day = match.group(2)
        hour = match.group(3)
        minute = match.group(4)
        second = match.group(5)

        date_string = f"{day} {month} {datetime.now().year} {hour}:{minute}:{second}"
        date_obj = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
        return date_obj


def get_pid(row):
    pid_regex = r'sshd\[(\d+)\]'
    match = re.search(pid_regex, row)
    if match:
        return int(match.group(1))


def get_user_from_log(row):
    user_regex = r'user (\w+)'
    match = re.search(user_regex, row)
    if match:
        return match.group(1)


def get_ipv4s_from_log(row):
    ip_regex = r'(?:\d{1,3}\.){3}\d{1,3}'
    match = re.findall(ip_regex, row)
    if match:
        try:
            return ipaddress.IPv4Address(match[0])
        except:
            return None
    return None


class SSHLogEntry(metaclass=ABCMeta):
    def __init__(self, log, message_type):
        self.date = get_date(log)
        self.user = get_user_from_log(log)
        self.ip_v4 = get_ipv4s_from_log(log)
        self.message_type = message_type
        self.pid = get_pid(log)
        self.entire_raw_log = log

    def __str__(self):
        return ("PID: " + str(self.pid) + " date: " + str(self.date) +
                (f" user: {str(self.user)}" if self.user is not None else "") +
                " ip_v4: " + str(self.ip_v4) + " message_type: " + str(self.message_type))

    @abstractmethod
    def validate(self):
        return (self.date == get_date(self.entire_raw_log)
                and self.user == get_user_from_log(self.entire_raw_log)
                and self.ip_v4 == get_ipv4s_from_log(self.entire_raw_log)
                and self.message_type == get_message_type(self.entire_raw_log)
                and self.pid == get_pid(self.entire_raw_log))

    def get_ip(self):
        return self.ip_v4

    @property
    def has_ip(self):
        return self.ip_v4 is not None

    def __repr__(self):
        return f"{self.__class__}, {self.__dict__}"

    # type hinting to access the _raw_log
    def __lt__(self, other: "SSHLogEntry"):
        return (self.pid, self.date, self.entire_raw_log) < (other.pid, other.date, other.entire_raw_log)

    def __gt__(self, other: "SSHLogEntry"):
        return (self.pid, self.date, self.entire_raw_log) > (other.pid, other.date, other.entire_raw_log)

    def __eq__(self, other):
        return not (self.__lt__(other) or self.__gt__(other))
