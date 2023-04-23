from ssh_log_entries import SSHLogPasswordDenied
from ssh_log_entries import SSHLogPasswordDenied
from SSHLogFactory import SSHLogFactory
from datetime import datetime
import ipaddress
import re
import sys
import utils


class SSHLogJournal:
    def __init__(self, entries=[]):
        self.entries = entries

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    def __contains__(self, item):
        return item in self.entries

    def append(self, log_entry: str):
        ssh_log = SSHLogFactory.get_log_entry(log_entry)

        if ssh_log.validate():
            self.entries.append(ssh_log)
            return True
        return False

    def filter_by_user(self, username=None):
        return [some_entry for some_entry in self.entries if some_entry.user == username]

    def __getattr__(self, name):
        if name.startswith("ip_"):
            # splits on non digits and then glue together with "." as separator, then turn to ip
            ip = ipaddress.IPv4Address(".".join(re.split(r"\D+", name[3:])))
            return [some_entry for some_entry in self.entries if some_entry.ip_v4 == ip]

        elif name.startswith("pid_"):
            pid = int(name[4:])
            return [some_entry for some_entry in self.entries if pid == some_entry.pid]

        elif name.startswith("date_"):
            # we only give the month and the day SO there will be more results :D
            day_and_month_regex = r"([A-Za-z]{3})(\D+)(\d+)"
            match = re.search(day_and_month_regex, name[5:])
            if not match:
                return

            month = match.group(1)
            day = match.group(3)
            date_obj = datetime.strptime(
                f"{day} {month} {datetime.now().year}", "%d %b %Y")
            return [some_entry for some_entry in self.entries if
                    (some_entry.date.month, some_entry.date.day) == (date_obj.month, date_obj.day)]

        else:
            raise AttributeError(
                f"'{type(self).__name__}' incorrect attribute '{name}'")

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return [self[i] for i in range(start, stop, step)]
        else:
            return self.entries[index]


if __name__ == "__main__":
    message0 = """Dec 28 06:55:33 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    test_log = SSHLogPasswordDenied.SSHLogPasswordDenied(message0)
    journal = SSHLogJournal()

    # load logs into journal

    for log in utils.read_logs(sys.argv[1]):
        journal.append(log)

    print(f"Before adding: {test_log in journal}")
    journal.append(message0)
    print(f"After adding: {test_log in journal}")
    print(f"First log: {journal[0]}")

    print(f"Iter: {iter(journal)}")
    print(f"Print every third of 12 logs {journal[0:12:3]}")

    print(journal.filter_by_user("xxchen"))

    print(f"Logs with ip_173_234_31_186: {journal.ip_173_234_31_186}")
    print(f"Logs with pid_24100: {journal.pid_24100}")
    print(f"Logs with date_Dec_28: {journal.date_Dec_28}")
