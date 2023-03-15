import sys
import file_printer
import line_validator


def calculate_all_files_size():
    bytes = 0
    for line in sys.stdin:
        if line_validator.validate_and_handle_exceptions(line):
            words = line.split()
            if words[-1] != "-":
                bytes += float(words[-1])

    file_printer.print_to_stdout(f"{bytes/10 ** 9:.2f} GB")


if __name__ == "__main__":
    calculate_all_files_size()
