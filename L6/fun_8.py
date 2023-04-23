from datetime import datetime

from SSHUser import SSHUser


def demonstrate(ssh_log_entry_list, ssh_log_journal_list):
    validation_list = ssh_log_entry_list + ssh_log_journal_list
    validation_list += SSHUser("A", datetime.now())

    for elem in validation_list:
        if not elem.validate():
            return False
    return True

# TODO to self: finish this fragment of code after other stuff is sufficiently finished
