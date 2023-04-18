def read_logs(file_path):
    with open(file_path, 'r') as file:
        for index, line in enumerate(file):
            line_dict = {index: line}
            yield line_dict

"""
# stream of logs, used as a generator for loops. Second version just generates one dictionary, so it will hang on
# reading the whole file for a while, before proceeding. First is recommended, but I left in both for testing,
# later we will delete one

def read_logs_v2(file_path):
    index = 0
    ssh_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            ssh_dict[index] = line
            index += 1
        return ssh_dict
"""

if __name__ == "__main__":
    # look at the difference
    path_to_file = "../L6/TEST.log"

    for i in read_logs(path_to_file):
        print(list(i.values())[0])
