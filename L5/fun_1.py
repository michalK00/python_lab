def read_logs(file_path):
    ssh_dict = {}
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            ssh_dict[i] = line
            i += 1
    return ssh_dict
