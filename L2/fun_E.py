import sys


def funE():
    for line in sys.stdin:
        words = line.split()
        code = words[-2]
        if code == "200":
            print(line, end="")


if __name__ == "__main__":
    funE()
