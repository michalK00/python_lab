import sys
import file_printer
import line_validator


def fild_largest_file():
    largest_file_size = 0
    largest_file_path = ""
    for line in sys.stdin:
        if line_validator.validate_and_handle_exceptions(line):
            words = line.split()
            if words[-1] != "-":
                bytes = int(words[-1])
                if largest_file_size < bytes:
                    largest_file_size = bytes
                    largest_file_path = words[-4]

    file_printer.print_to_stdout(
        f"File path: {largest_file_path}, {largest_file_size/10 ** 6:.2f} MB")


if __name__ == "__main__":
    fild_largest_file()
