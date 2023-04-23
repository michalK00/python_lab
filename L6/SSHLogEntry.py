import re
import datetime
import type_enum as ms
import ipaddress
import abc


class SSHLogEntry(metaclass=abc.ABCMeta):

    def __init__(self, log):
        self.date = self.get_date(log)
        self.user = self.get_user_from_log(log)
        self.ip_v4 = self.get_ipv4s_from_log(log)
        self.message_type = self.get_message_type(log)
        self.pid = self.get_pid(log)
        self._raw_log = log

    def __str__(self):
        return "PID: " + self.pid + " date: " + self.date + \
            (" user: " + self.user if self.user is not None else "") + \
            " ip_v4: " + self.ip_v4 + " message_type: " + self.message_type

    def _ip_exists(self):
        return self.ip_v4 is not None

    @abc.abstractmethod
    def validate(self):
        pass

    def get_ipv4(self):
        return self.ip_v4

    has_ip = property(fget=_ip_exists)

    def get_message_type(row):
        pass_acc = "Accepted password"
        pass_den = "Failed password"
        error = "error:"

        if re.search(pass_acc, row):
            return ms.PASSWORD_ACCEPTED
        elif re.search(pass_den, row):
            return ms.PASSWORD_DENIED
        elif re.search(error, row):
            return ms.ERROR
        else:
            return ms.OTHER

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
            return match.group(1)

    def get_user_from_log(row):
        user_regex = r'user (\w+)'
        match = re.search(user_regex, row)
        if match:
            return match.group(1)

    def get_ipv4s_from_log(row):
        ip_regex = r'(?:\d{1,3}\.){3}\d{1,3}'
        match = re.findall(ip_regex, row)
        if match:
            return ipaddress.IPv4Address(match)
        return None
