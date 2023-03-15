import sys
import fun_A_base as base
import file_printer
import line_validator


def count_code_302():
    number_of_302 = 0
    for line in sys.stdin:
        if line_validator.validate_and_handle_exceptions(line):
            number_of_302 = base.count_code_base(line, "302", number_of_302,)
    file_printer.print_to_stdout(f"Number of codes 302: {number_of_302}")


if __name__ == "__main__":
    count_code_302()
