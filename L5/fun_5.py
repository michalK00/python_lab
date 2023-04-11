import argparse
import logging
import os
from typing import Optional, Sequence

import fun_3
import fun_1


def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(description="L5 arg parser")

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
    subparser_additional_functions.add_parser("fun_4_a", help="calls fun_4_a")
    subparser_additional_functions.add_parser("fun_4_b", help="calls fun_4_b")
    subparser_additional_functions.add_parser("fun_4_c", help="calls fun_4_c")
    subparser_additional_functions.add_parser("fun_4_d", help="calls fun_4_d")

    args = parser.parse_args(argv)
    # print(vars(args))
    # print(args.logfile_path)
    # print(args.other_function)

    if os.path.isfile(parsed_path := os.path.abspath(args.logfile_path)):
        line_generator = fun_1.read_logs(parsed_path)
    else:
        raise ValueError(f"{parsed_path} does not exist!")

    fun_3.change_min_logging_level(args.minlevel)

    for line in line_generator:
        fun_3.check_message_type(...)   # correctly parsed message

    match args.other_function:  # calling functions
        case "fun_2_b":
            ...
        case "fun_2_c":
            ...
        case "fun_4_a":
            ...
        case "fun_4_b":
            ...
        case "fun_4_c":
            ...
        case "fun_4_d":
            ...
        case _:
            pass


if __name__ == "__main__":
    exit(main())
