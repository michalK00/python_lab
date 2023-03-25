import re
import sys
import fun_A as Reader
import fun_G as Printer
import console_input_checker


def get_entries_by_addr(logs, address):
    if validate_address(address):
        filtered_iterator = filter(lambda entry: entry[0] == address, logs)
        return list(filtered_iterator)
    else:
        return list()


def validate_address(address):
    return True if re.search("[^A-Za-z0-9!$&\'+,;@:?#_.~*()%=-\[\]]", address) is None else False


if __name__ == "__main__":
    console_input_checker.check_console_input("Input URL", lambda: Printer.print_entries(
        get_entries_by_addr(Reader.read_logs(), sys.argv[1])))
