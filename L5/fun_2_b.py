import re

# zwraca listę ale w tych logach nie ma takich wierszy z dwoma lub więcej adresami


def get_ipv4s_from_log(row):
    ip_regex = r'(?:\d{1,3}\.){3}\d{1,3}'
    match = re.findall(ip_regex, row)
    if match:
        return match
    return None
