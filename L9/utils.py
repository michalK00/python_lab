def read_logs(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
