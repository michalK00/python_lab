def get_entries_by_code(list_of_tuples, status_code):
    if not status_code.isnumeric():
        return

    list_of_accepted_tuples = []

    for tuple_of_log in list_of_tuples:  # (url, date, path, status_code, bit_size)
        if tuple_of_log[3] == status_code:
            list_of_accepted_tuples += tuple_of_log

    return list_of_accepted_tuples
