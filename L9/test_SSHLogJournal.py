from SSHLogJournal import SSHLogJournal
from SSHLogError import SSHLogError
from SSHLogOther import SSHLogOther
from SSHLogPasswordAccepted import SSHLogPasswordAccepted
from SSHLogPasswordDenied import SSHLogPasswordDenied
import pytest


@pytest.mark.parametrize("log, expectedType", [
    ("Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2",
     SSHLogPasswordAccepted),
    ("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2", SSHLogPasswordDenied),
    ("Dec 10 07:51:15 LabSZ sshd[24324]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]", SSHLogError),
    ("Dec 10 07:51:12 LabSZ sshd[24324]: pam_unix(sshd:auth): check pass; user unknown", SSHLogOther)
])
def test_append(log, expectedType):
    journal: SSHLogJournal = SSHLogJournal([])
    journal.append(log)
    assert type(journal[0]) is expectedType
