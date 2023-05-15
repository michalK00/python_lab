from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg


class SSHLogPasswordDenied(SSHLogEntry):
    def __init__(self, log: str):
        super().__init__(log, Msg.PASSWORD_DENIED)

    def validate(self) -> bool:
        return super().validate()


if __name__ == "__main__":
    message0: str = (
        "Dec 20 06:55:48 LabSZ sshd[24100]: "
        "Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"
    )
    ssh_obj0: SSHLogPasswordDenied = SSHLogPasswordDenied(message0)
    ssh_obj1: SSHLogPasswordDenied = SSHLogPasswordDenied(message0)

    print(f"Should be equal: {ssh_obj0 == ssh_obj1}")

    message1: str = (
        "Dec 10 06:55:48 LabSZ sshd[24100]: "
        "Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"
    )
