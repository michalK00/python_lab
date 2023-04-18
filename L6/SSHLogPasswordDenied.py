import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogPasswordDenied(SSHLogEntry.SSHLogEntry):
    def __init__(self, log):
        super().__init__(log, Msg.PASSWORD_DENIED)

    def validate(self):
        return super().validate()


if __name__ == "__main__":
    message0 = """Dec 1 06:55:48 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    message1 = """Dec 10 06:55:48 LabSZ sshd[24100]: 
        Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"""
    someObj0 = SSHLogPasswordDenied(message0)
    someObj1 = SSHLogPasswordDenied(message1)
    # print(someObj0)
    print(someObj0 < someObj1)
