import sys


def funB():
    bytes = 0
    for line in sys.stdin:
        words = line.split()
        if words[-1] != "-":
            bytes += float(words[-1])

    print(f"{bytes/10 ** 9:.2f} GB")


if __name__ == "__main__":
    funB()
