import re


def getNamedTuple(row):
    date_regex = "([A-z]{3}) (0?[1-9]|[12][0-9]|3[01]) (?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)"
    print(row.split(" "))


getNamedTuple(
    "Dec 30 06:17:30 LabSZ sshd[11536]: Received disconnect from 139.219.191.138: 11: Bye Bye [preauth]")
