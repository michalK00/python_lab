import re
import datetime
import line_validator

date_dictionary = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
                   "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                   "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def validate_friday(line, line_num):
    date = re.split("[\s/:]", re.findall("(?<=\[)(.*)(?=\])",
                    line_validator.validate_line_to_standard(line, line_num))[0])
    if datetime.datetime(int(date[2]), date_dictionary[date[1]], int(date[0])).weekday() == 4:
        print(line, end="")
