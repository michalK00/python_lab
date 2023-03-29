import os
import fun_2_a


def find_execs(path_string):
    if os.path.exists(os.path.abspath(path_string)):
        return path_string, [elem for elem in os.listdir(path_string) if
                             os.access(os.path.join(os.path.abspath(path_string), elem), mode=os.X_OK & os.F_OK)]


if __name__ == "__main__":
    for parsed_path in fun_2_a.parse_path():
        print(find_execs(parsed_path))
