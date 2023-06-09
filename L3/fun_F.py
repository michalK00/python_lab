import fun_A
import fun_G
import sys
import console_input_checker


def get_entries_extension(list_of_tuples, extension):
    correct_extensions_list = []

    for log_tuple in list_of_tuples:
        if str(log_tuple[2]).find(extension) != -1:
            correct_extensions_list.append(log_tuple)

    return correct_extensions_list


if __name__ == "__main__":
    console_input_checker.check_console_input("Input extension", lambda: fun_G.print_entries(
        get_entries_extension(fun_A.read_logs(), sys.argv[1])))
