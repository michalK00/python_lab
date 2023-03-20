import sys
import line_validator
import re
import datetime


def read_logs():
    logs = []
    for line in sys.stdin:
        try:
            line_validator.validate_line_to_standard(line)
        except Exception as err:
            pass
        else:

            url = re.search("^(.+?) -", line)
            date_split = re.split("[\s/:]", re.findall("(?<=\[)(.*)(?=\])", line)[0])
            date = datetime.datetime(int(date_split[2]), datetime.datetime.strptime(date_split[1], "%b").month,
                                     int(date_split[0]))
            path = re.findall("(?<=\")(.*)(?=\")", line)[0]

            words = line.split()
            bit_size = int(words.pop())
            error_message = int(words.pop())

            logs += (url, date, path, error_message, bit_size)

    return logs
