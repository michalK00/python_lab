import re


def get_entries_by_addr(logs, address):
    if (validate_address(address)):
        filtered = filter(lambda entry: entry[0] == address, logs)
        return list(filtered)
    else:
        return list()


def validate_address(address):
    if not (re.search("[^A-Za-z0-9!$&\'+,;@:?#_.~*()%=-\[\]]", address) is None):
        return False
    else:
        return True


if __name__ == "__main__":
    print(get_entries_by_addr(
        [("192.168.0.1", "log1"), ("ad€am", "log2")], "ad€am"))
