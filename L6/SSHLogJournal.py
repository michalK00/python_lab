import SSHLogPasswordDenied
import SSHLogEntry as ssh
import type_enum as msg
from SSHLogFactory import *
import SSHLogEntry
from datetime import datetime


class SSHLogJournal:
    def __init__(self, entries=[]):
        self.entries = entries

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    def __contains__(self, item):
        return item in self.entries

    def _parse_to_log(self, log: str) -> SSHLogEntry:
        message_type = ssh.get_message_type(log)
        match message_type:
            case msg.TypeOfMessage.ERROR:
                return SSHErrorLogFactory.create_ssh_entry_obj(log)
            case msg.TypeOfMessage.OTHER:
                return SSHOtherLogFactory.create_ssh_entry_obj(log)
            case msg.TypeOfMessage.PASSWORD_ACCEPTED:
                return SSHPasswordAcceptedLogFactory.create_ssh_entry_obj(
                    log)
            case msg.TypeOfMessage.PASSWORD_DENIED:
                return SSHPasswordDeniedLogFactory.create_ssh_entry_obj(log)

    def append(self, log: str):
        ssh_log = self._parse_to_log(log)

        if ssh_log.validate():
            self.entries.append(ssh_log)
            return True
        return False

    def filter_by_user(self, username=None):
        if username is None:
            return [entry for entry in self.entries if entry.user == None]
        else:
            return [entry for entry in self.entries if entry.user == username]

    # doesn't work
    # def __getattr__(self, name):
    #     if name.startswith("ip_"):
    #         ip = name[3:]
    #         return [entry for entry in self.entries if entry.ip_v4 == ip]
    #     elif name.startswith("pid_"):
    #         pid = int(name[6:])
    #         return [entry for entry in self.entries if entry.pid == pid]
    #     elif name.startswith("date_"):
    #         date_str = name[5:]
    #         date = datetime.strptime(date_str, "%Y-%m-%d")
    #         return [entry for entry in self.entries if entry.date == date]
    #     else:
    #         raise AttributeError(
    #             f"'{type(self).__name__}' object has no attribute '{name}'")

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            return [self[i] for i in range(start, stop, step)]
        else:
            return self.entries[index]


if __name__ == "__main__":
    message0 = """Dec 20 06:55:33 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    message1 = """Dec 10 06:55:48 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    message2 = """Dec 31 23:56:28 LabSZ sshd[3101]: Invalid user vyatta from 202.107.207.123"""
    log = SSHLogPasswordDenied.SSHLogPasswordDenied(message0)
    journal = SSHLogJournal()
    journal.append(message0)
    journal.append(message1)
    journal.append(message2)
    print(journal[0])
    print(log in journal)
    print(len(journal))
    print(iter(journal))
    print(journal[0:1:1])
