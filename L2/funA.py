import sys


def funA():
    codes = {200: 0, 302: 0, 404: 0, "undefined": 0}
    for line in sys.stdin:
        words = line.split()
        code = int(words[-2])
        if code in codes:
            codes[code] += 1
        else:
            codes["undefined"] += 1

    print(codes)


if __name__ == "__main__":
    funA()
