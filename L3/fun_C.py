import re
import fun_A as reader
import fun_G as printer


def get_entries_by_addr(logs, address):
    if validate_address(address):
        filtered_iterator = filter(lambda entry: entry[0] == address, logs)
        return list(filtered_iterator)
    else:
        return list()


def validate_address(address):
    return True if re.search("[^A-Za-z0-9!$&\'+,;@:?#_.~*()%=-\[\]]", address) is None else False


if __name__ == "__main__":
    printer.print_entries(get_entries_by_addr(reader.read_logs(), "199.120.110.21"))
