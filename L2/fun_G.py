import re
import datetime
import file_printer
import file_reader


date_dictionary = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
                   "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
                   "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def validate_friday(line):
    date = re.split("[\s/:]", re.findall("(?<=\[)(.*)(?=\])",line)[0])
    if datetime.datetime(int(date[2]), date_dictionary[date[1]], int(date[0])).weekday() == 4:
        file_printer.print_to_stdout(line)


if __name__ == "__main__":
    file_reader.read_file_from_stdin(validate_friday)
