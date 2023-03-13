import sys
import funA_base


def funA():
    number_of_302 = 0
    for line in sys.stdin:
        number_of_302 = funA_base.funA(line, "302", number_of_302,)
    print(f"Number of codes 302: {number_of_302}")


if __name__ == "__main__":
    funA()
