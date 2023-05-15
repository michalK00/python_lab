from datetime import datetime
from typing import List, Protocol

from SSHLogEntry import SSHLogEntry
from SSHUser import SSHUser
from SSHLogJournal import SSHLogJournal
from SSHLogFactory import SSHLogFactory


class SupportsValidation(Protocol):
    def validate(self) -> bool:
        pass


def demonstrate(
    log_entries: List[SSHLogEntry], log_journal: SSHLogJournal, log_users: List[SSHUser]
) -> bool:
    validation_list: List[SupportsValidation] = []
    validation_list += log_entries
    validation_list += log_journal
    validation_list += log_users

    for elem in validation_list:
        if elem is None or not elem.validate():
            return False
    return True


if __name__ == "__main__":
    message0: str = (
        "Dec 20 06:55:33 LabSZ sshd[24100]: "
        "Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"
    )
    message1: str = (
        "Dec 10 06:55:48 LabSZ sshd[24100]: "
        "Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"
    )
    message2: str = (
        "Dec 31 23:56:28 LabSZ sshd[3101]: " "Invalid user vyatta from 202.107.207.123"
    )

    journal: SSHLogJournal = SSHLogJournal([])
    journal.append(message0)
    journal.append(message1)
    journal.append(message2)

    logs: List[SSHLogEntry] = [
        SSHLogFactory.get_log_entry(message0),
        SSHLogFactory.get_log_entry(message1),
        SSHLogFactory.get_log_entry(message2),
    ]

    users: List[SSHUser] = [
        SSHUser("a", datetime.now()),
        SSHUser("_testimony", datetime.now()),
    ]

    print(f"Did duck-typing work: {demonstrate(logs, journal, users)}")
