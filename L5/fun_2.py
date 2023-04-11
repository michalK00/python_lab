import re
from datetime import datetime

# nie zwraca listy tylko po prostu adres bo w tych logach nie ma takich wierszy z dwoma lub więcej adresami


def get_ipv4s_from_log(row):
    ip_regex = r'(?:\d{1,3}\.){3}\d{1,3}'
    match = re.findall(ip_regex, row)
    if match:
        return match
    return None


def get_user_from_log(row):
    user_regex = r'user (\w+)'
    match = re.search(user_regex, row)
    if match:
        return match.group(1)
    return None


def get_message_type(row):
    # tutaj nie wiem bo nie ma żadnych logów z pomyślnym logowaniem
    successful_login = "Login successful"
    failed_login = "Received disconnect"
    connection_closed = "Connection closed"
    wrong_password = "Failed password"
    wrong_login = "Invalid user"
    break_in_attempt = "POSSIBLE BREAK-IN ATTEMPT!"
    if re.search(successful_login, row):
        return "SUCCESSFUL_LOGIN"
    elif re.search(failed_login, row):
        return "FAILED_LOGIN"
    elif re.search(connection_closed, row):
        return "CONNECTION_CLOSED"
    elif re.search(wrong_password, row):
        return "WRONG_PASSWORD"
    elif re.search(wrong_login, row):
        return "WRONG_LOGIN"
    elif re.search(break_in_attempt, row):
        return "BREAK_IN_ATTEMPT"
    else:
        return "OTHER"


def get_date(row):
    date_regex = r'([A-z]{3}) (0?[1-9]|[12][0-9]|3[01]) (?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)'
    match = re.search(date_regex, row)
    if match:

        month = match.group(1)
        day = match.group(2)
        hour = match.group(3)
        minute = match.group(4)
        second = match.group(5)

        # Create a datetime object
        date_string = f"{day} {month} {datetime.now().year} {hour}:{minute}:{second}"
        date_obj = datetime.strptime(date_string, "%d %b %Y %H:%M:%S")
        return date_obj
    else:
        return None


def get_message(row):
    capture_message = r'sshd\[\d+\]:(.+)'
    return re.search(capture_message, row).group(1)


def getDict(row):
    row_dict = {
        "date": get_date(row),
        "user": get_user_from_log(row),
        "ip_v4": get_ipv4s_from_log(row),
        "type": get_message_type(row),
        "message": get_message(row)
    }
    print(row_dict)


getDict(
    "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]")
