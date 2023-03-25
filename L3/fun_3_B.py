import fun_A
import fun_G
import fun_3_A


def log_to_dict(list_of_tuples):
    dictionary_of_ips = {}

    for tuple_log in list_of_tuples:
        if tuple_log[0] in dictionary_of_ips:
            dictionary_of_ips[tuple_log[0]].append(
                fun_3_A.entry_to_dict(tuple_log))
        else:
            dictionary_of_ips[tuple_log[0]] = list()
            dictionary_of_ips[tuple_log[0]].append(
                fun_3_A.entry_to_dict(tuple_log))
    return dictionary_of_ips


if __name__ == "__main__":
    print(log_to_dict(fun_A.read_logs()))
