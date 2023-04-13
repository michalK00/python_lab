import argparse
import logging
import os
from typing import Optional, Sequence
from functools import partial

import fun_1
import fun_2
import fun_2_b
import fun_2_c
import fun_3
import fun_4_a
import fun_4_b
import fun_4_c


def call_and_print_in_loop(a_fun, parsed_path):
    for line in fun_1.read_logs(parsed_path):
        if (res := a_fun(list(line.values())[0])) is not None:
            print(res)


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(description="L5 args parser")

    # positional arguments:
    parser.add_argument(
        "logfile_path", help="states a path to the file with SSH logs")

    # options:
    parser.add_argument("-m", "--minlevel", help="states the minimal level of logging (default: %(default)s)",
                        default=logging.DEBUG, type=int,
                        choices=(logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL))

    # subcommands (you cant have multiple subparsers, you can only nest them)
    subparser_additional_functions = parser.add_subparsers(title="call functions from other exercises",
                                                           description="subcommands for calling fun_2",
                                                           dest="other_function")
    subparser_additional_functions.add_parser("fun_2_b", help="calls fun_2_b")
    subparser_additional_functions.add_parser("fun_2_c", help="calls fun_2_c")
    subparser_additional_functions.add_parser("fun_2_d", help="calls fun_2_d")
    subparser_additional_functions.add_parser("fun_4_a", help="calls fun_4_a")
    subparser_additional_functions.add_parser("fun_4_b", help="calls fun_4_b")
    subparser_additional_functions.add_parser("fun_4_c", help="calls fun_4_c")
    # subparser_additional_functions.add_parser("fun_4_d", help="calls fun_4_d")

    args = parser.parse_args(argv)

    fun_3.change_min_logging_level(args.minlevel)

    if not os.path.isfile(parsed_path := os.path.abspath(args.logfile_path)):
        raise ValueError(f"{parsed_path} does not exist!")

    call = partial(call_and_print_in_loop, parsed_path=parsed_path)

    match args.other_function:  # calling functions
        case "fun_2_b":
            call(fun_2_b.get_ipv4s_from_log)
        case "fun_2_c":
            call(fun_2_c.get_user_from_log)
        case "fun_2_d":
            call(fun_2.get_message_type)
        case "fun_4_a":
            print(fun_4_a.get_n_random_rows_from_random_user(5, parsed_path))  # TODO: line amount reading
        case "fun_4_b":
            print(fun_4_b.calculate_globally(parsed_path))
            print(fun_4_b.calculate_locally(parsed_path))
        case "fun_4_c":
            print(fun_4_c.users_who_logged_in_least_and_most_frequently(parsed_path))
        case _:
            # doing it only if no other function is to be called
            for line in fun_1.read_logs(parsed_path):
                fun_3.check_message_type(fun_2.get_row_dict(list(line.values())[0]))


if __name__ == "__main__":
    exit(main())
