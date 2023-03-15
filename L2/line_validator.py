import re

# declared outside, so it doesn't have to be initialized with every new line
date_dictionary = {"Jan": 31, "Feb": 29, "Mar": 31, "Apr": 30,
                   "May": 31, "Jun": 30, "Jul": 31, "Aug": 31,
                   "Sep": 30, "Oct": 31, "Nov": 30, "Dec": 31}


def validate_line_to_standard(line):
    line_stamp = f"\"{line}\""
    words = line.split()

    # if len(words) != 10:
    #    raise Exception("Incorrect formatting at line: " + line_stamp)

    url = line.split("-")[0][:-1]
    # checking if characters are correct for URL/host address
    if not (re.search("[^A-Za-z0-9!$&\'+,;@:?#_.~*()%=-\[\]]", url) is None):
        raise Exception("Incorrect format of URL/Hostname at line " + line_stamp)

    # splitting the date to check it (without leap years)
    date = re.split("[\s/:]", re.findall("(?<=\[)(.*)(?=\])", line)[0])  # this finds the date and splits it
    # checking if months and days are correctly correlated
    if len(date) != 7 or any(int(num) < 0 for num in date[:1] + date[2:6]) or not (
            date[1] in date_dictionary and date_dictionary[date[1]] >= int(date[0])):
        raise Exception("Incorrect date at line: " + line_stamp)

    # if hours, minutes and seconds have correct format
    if int(date[3]) > 24 or int(date[4]) > 60 or int(date[5]) > 60:
        raise Exception("Incorrect time at line: " + line_stamp)

    # I check only the correctness of characters, as there isn't any set path or HTML method
    path = re.findall("(?<=\")(.*)(?=\")", line)[0]
    if not (re.search("[<>\"|\\?*:]", path) is None):
        raise Exception("Incorrect path at line " + line_stamp)

    # check if bit size and error number are correct
    bit_size = words.pop()
    error_message = words.pop()

    if not (error_message == "404" or bit_size == "-"):
        try:
            bit_size_num = int(bit_size)
        except ValueError as err:
            raise Exception("Error code and bit size must be numbers if error is not 404 " + line_stamp) from err
        else:
            if bit_size_num < 0:
                raise Exception("Bit size must be positive" + line_stamp)

    return line
