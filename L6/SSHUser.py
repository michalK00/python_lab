import re


class SSHUser:
    def __init__(self, user_name, last_login_date):
        self.user_name = user_name
        self.last_login_date = last_login_date

    def validate(self):
        user_name_regex = r"^[a-z_][a-z0-9_-]{0,31}$"
        return re.search(user_name_regex, self.user_name)
