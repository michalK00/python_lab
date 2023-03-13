import sys


def funF():
    for line in sys.stdin:
        words = line.split()
        time_stamp = words[3]
        hour = int((time_stamp.split(":"))[1])
        if hour > 22 or hour < 6:
            print(line, end="")


if __name__ == "__main__":
    funF()
