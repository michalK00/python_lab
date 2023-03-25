import fun_A as reader


def sort_log(logs, param):
    # sort function returns nothing and makes changes to the original sequence,
    # while the sorted() function creates a new sequence type
    # containing a sorted version of the given sequence
    try:
        logs.sort(key=lambda log: log[param])
        return logs
    except IndexError:
        return "Index out of range"


if __name__ == "__main__":
    sort_log(reader.read_logs(), -2)
