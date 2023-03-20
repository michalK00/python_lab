import fun_A as reader


def sort_log(logs, param):

    # sorted_logs = sorted(logs, key=lambda log: log[param])
    logs.sort(key=lambda log: log[param])
    print(logs)


if __name__ == "__main__":
    sort_log(reader.read_logs(), -1)
