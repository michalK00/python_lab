from datetime import datetime

from SSHUser import SSHUser
from SSHLogJournal import SSHLogJournal
from SSHLogFactory import SSHLogFactory


def demonstrate(ssh_log_entry_list, ssh_log_journal, ssh_users_list):
    validation_list = ssh_log_entry_list + ssh_log_journal.entries + ssh_users_list

    for elem in validation_list:
        if not elem.validate():
            return False
    return True


if __name__ == "__main__":
    message0 = """Dec 20 06:55:33 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    message1 = """Dec 10 06:55:48 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    message2 = """Dec 31 23:56:28 LabSZ sshd[3101]: Invalid user vyatta from 202.107.207.123"""

    journal = SSHLogJournal()
    journal.append(message0)
    journal.append(message1)
    journal.append(message2)

    logs = [SSHLogFactory.get_log_entry(message0), SSHLogFactory.get_log_entry(message1),
            SSHLogFactory.get_log_entry(message2)]

    users = [SSHUser("a", datetime.now()), SSHUser("_testimoney", datetime.now())]

    print(f"Did ducktyping work: {demonstrate(logs, journal, users)}")
