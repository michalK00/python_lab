from typing import Generator
from datetime import datetime

from SSHLogFactory import SSHLogFactory
from SSHLogEntry import SSHLogEntry


log_list = []


# Generator[yield_type, send_type, return type]
def gather_logs(file_path: str) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            log_list.append(SSHLogFactory.get_log_entry(line))


def get_logs() -> Generator[str, None, None]:
    for log in log_list:
        yield log.entire_raw_log


def get_logs_between_dates(start_date: datetime, end_date: datetime) -> Generator[str, None, None]:
    for log in log_list:
        if start_date <= log.date <= end_date:
            yield log.entire_raw_log

