import re


def get_user_from_log(row):
    user_regex = r'user (\w+)'
    match = re.search(user_regex, row)
    if match:
        return match.group(1)
    return None
