import sys
import fun_A_base as base
import file_printer
import line_validator


def count_code_200():
    number_of_200 = 0
    for line in sys.stdin:
        if line_validator.validate_and_handle_exceptions(line):
            number_of_200 = base.count_code_base(line, "200", number_of_200,)
    file_printer.print_to_stdout(f"Number of codes 200: {number_of_200}")


if __name__ == "__main__":
    count_code_200()
