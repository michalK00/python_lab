import re
from datetime import datetime
from fun_1 import read_logs
from fun_2_b import get_ipv4s_from_log
from fun_2_c import get_user_from_log
from type_enum import TypeOfMessage as ms


def get_message_type(row):
    successful_login = "session opened"
    failed_login = "authentication failure"
    connection_closed = "session closed"
    wrong_password = "Failed password"
    wrong_user = "Invalid user"
    break_in_attempt = "POSSIBLE BREAK-IN ATTEMPT!"

    if re.search(successful_login, row):
        return ms.LOGIN_SUCCESSFUL
    elif re.search(failed_login, row):
        return ms.LOGIN_FAILURE
    elif re.search(connection_closed, row):
        return ms.CONNECTION_CLOSED
    elif re.search(wrong_password, row):
        return ms.WRONG_PASSWORD
    elif re.search(wrong_user, row):
        return ms.WRONG_USER
    elif re.search(break_in_attempt, row):
        return ms.BREAK_IN_ATTEMPT
    else:
        return ms.OTHER


def get_sshd(row):
    sshd_regex = r'sshd\[(\d+)\]'
    match = re.search(sshd_regex, row)
    if match:
        sshd = match.group(1)
    return sshd


def get_date(row):
    date_regex = r'([A-z]{3})\s+(0?[1-9]|[12][0-9]|3[01]) (?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)'
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


def get_row_dict(row):
    row_dict = {
        "date": get_date(row),
        "user": get_user_from_log(row),
        "ip_v4": get_ipv4s_from_log(row),
        "type": get_message_type(row),
        "message": get_message(row),
        "sshd": get_sshd(row)
    }
    return row_dict


def to_list_of_dicts(path):
    return [get_row_dict(row[count]) for count, row in enumerate(read_logs(path))]
