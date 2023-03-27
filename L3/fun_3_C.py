import fun_3_B
import fun_A


def get_addrs(dictionary_of_ips):
    list_of_addrs = []
    for key in dictionary_of_ips.keys():
        list_of_addrs.append(key)

    return list_of_addrs


if __name__ == "__main__":
    print(get_addrs(fun_3_B.log_to_dict(fun_A.read_logs())))
