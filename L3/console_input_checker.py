import sys


def check_console_input(possible_error, fun):
    if len(sys.argv) < 2:
        raise Exception(possible_error)
    else:
        fun()
