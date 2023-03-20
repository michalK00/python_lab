def get_failed_reads(list_of_tuples, if_joined_lists=True):
    list_of_4xx = []
    list_of_5xx = []

    for tuple_of_log in list_of_tuples:  # (url, date, path, status_code, bit_size)
        if tuple_of_log % 100 == 4:
            list_of_4xx += tuple_of_log
        elif tuple_of_log % 100 == 5:
            list_of_5xx += tuple_of_log

    if if_joined_lists:
        return list_of_4xx.extend(list_of_5xx)
    else:
        return list_of_4xx, list_of_5xx
