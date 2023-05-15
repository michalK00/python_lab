import re
from datetime import datetime


class SSHUser:
    def __init__(self, user_name: str, last_login_date: datetime):
        self.user_name: str = user_name
        self.last_login_date: datetime = last_login_date

    def validate(self) -> bool:
        # ^ - starts at the beginning, makes sure that there aren't incorrect chars there
        # [a-z_] - first char is a lower case letter or a _
        # [a-z0-9_-]{0,31} - up to 31 chars that are letters, numbers or _
        # $ - asserts position at the end. makes sure that there aren't any incorrect chars after the correct ones
        user_name_regex: str = r"^[a-z_][a-z0-9_-]{0,31}$"
        return bool(re.search(user_name_regex, self.user_name))
