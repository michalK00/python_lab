import fun_A
import fun_G
import sys
import console_input_checker


def get_entries_by_code(list_of_tuples, status_code):
    if not str(status_code).isnumeric():
        return []

    status_code_int = int(status_code)
    list_of_accepted_tuples = []

    for tuple_of_log in list_of_tuples:  # (url, date, path, status_code, bit_size)
        if tuple_of_log[3] == status_code_int:
            list_of_accepted_tuples.append(tuple_of_log)

    return list_of_accepted_tuples


if __name__ == "__main__":
    console_input_checker.check_console_input("Input code", lambda: fun_G.print_entries(
        get_entries_by_code(fun_A.read_logs(), sys.argv[1])))
