import sys
import fun_A_base as base


def funA():
    number_of_404 = 0
    for line in sys.stdin:
        number_of_404 = base.funA(line, "404", number_of_404,)
    print(f"Number of codes 404: {number_of_404}")


if __name__ == "__main__":
    funA()
