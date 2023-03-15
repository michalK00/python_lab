import sys
import fun_A_base as base


def funA():
    number_of_200 = 0
    for line in sys.stdin:
        number_of_200 = base.funA(line, "200", number_of_200,)
    return f"Number of codes 200: {number_of_200}"


if __name__ == "__main__":
    funA()
