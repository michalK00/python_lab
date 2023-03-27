import os
import fun_2_a


def find_execs(path_string):
    return path_string, [elem for elem in os.listdir(path_string) if
                         os.access(os.path.join(path_string, elem), mode=os.F_OK & os.F_OK)]


if __name__ == "__main__":
    for path in fun_2_a.parse_path():
        print(find_execs(path))