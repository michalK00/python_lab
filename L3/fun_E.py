import fun_G
import fun_A


def get_failed_reads(list_of_tuples, if_extended_lists=True):
    list_of_4xx = []
    list_of_5xx = []

    for tuple_of_log in list_of_tuples:  # (url, date, path, status_code, bit_size)
        if tuple_of_log[3] // 100 == 4:
            list_of_4xx.append(tuple_of_log)
        elif tuple_of_log[3] // 100 == 5:
            list_of_5xx.append(tuple_of_log)

    if if_extended_lists:
        return list_of_4xx + list_of_5xx
    else:
        return list_of_4xx, list_of_5xx


if __name__ == "__main__":
    fun_G.print_entries(get_failed_reads(fun_A.read_logs(), True))
