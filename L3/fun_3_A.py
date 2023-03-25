import fun_A


def entry_to_dict(tuple_log):
    dictionary_of_log = {"url/ip": tuple_log[0],
                         "datetime": tuple_log[1],
                         "path": tuple_log[2],
                         "status_code": tuple_log[3],
                         "bit_size": tuple_log[4]}
    return dictionary_of_log


if __name__ == "__main__":
    for log in fun_A.read_logs():
        print(entry_to_dict(log))
