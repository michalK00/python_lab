import sys
import funA_base


def funA():
    number_of_200 = 0
    for line in sys.stdin:
        number_of_200 = funA_base.funA(line, "200", number_of_200,)
    print(f"Number of codes 200: {number_of_200}")


if __name__ == "__main__":
    funA()
