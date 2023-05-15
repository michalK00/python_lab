from typing import Generator


def read_logs(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as file:
        for line in file:
            yield line
