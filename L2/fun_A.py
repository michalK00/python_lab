import sys
import file_printer
import line_validator


def count_all_codes():
    codes = {200: 0, 302: 0, 404: 0, "undefined": 0}
    for line in sys.stdin:
        if line_validator.validate_and_handle_exceptions(line):
            words = line.split()
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
            else:
                codes["undefined"] += 1

    file_printer.print_to_stdout(codes)


if __name__ == "__main__":
    count_all_codes()
