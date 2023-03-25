import re
import sys
import fun_G
import fun_A as reader


def get_entries_by_addr(logs, address):
    if (validate_address(address)):
        filtered_iterator = filter(lambda entry: entry[0] == address, logs)
        return list(filtered_iterator)
    else:
        return list()


def validate_address(address):
    if (re.search("[^A-Za-z0-9!$&\'+,;@:?#_.~*()%=-\[\]]", address) is None):
        return False
    else:
        return True


if __name__ == "__main__":
    fun_G.print_entries(get_entries_by_addr(reader.read_logs(), sys.argv[1]))
