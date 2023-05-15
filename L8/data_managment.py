from typing import Generator, Tuple, List
from datetime import datetime
import ipaddress as ip

from SSHLogFactory import SSHLogFactory
from SSHLogEntry import SSHLogEntry
from type_enum import TypeOfMessage as Msg

_log_list: List[SSHLogEntry] = []
_filtered_log_list: List[SSHLogEntry] = []


# Generator[yield_type, send_type, return type]
def gather_logs(file_path: str) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            _log_list.append(SSHLogFactory.get_log_entry(line))


def get_logs() -> Generator[str, None, None]:
    for log in _log_list:
        yield log.entire_raw_log[0:65] + "..."
        # yield log.entire_raw_log


def get_logs_between_dates(start_date: datetime, end_date: datetime) -> Generator[str, None, None]:
    _filtered_log_list.clear()
    for log in _log_list:
        if start_date <= log.date <= end_date:
            _filtered_log_list.append(log)
            yield log.entire_raw_log[0:65] + "..."


def get_item_from_log_list(index: int) -> Tuple[datetime, str, ip.ip_address, Msg, int]:
    return _get_item_from_list(index, _log_list)


def get_item_from_filtered_list(index: int) -> Tuple[datetime, str, ip.ip_address, Msg, int]:
    return _get_item_from_list(index, _filtered_log_list)


def _get_item_from_list(index: int, list_of_logs: List[SSHLogEntry]) -> Tuple[datetime, str, ip.ip_address, Msg, int]:
    if 0 <= index < len(list_of_logs):
        temp: SSHLogEntry = list_of_logs[index]
        return temp.date, temp.user, temp.ip_v4, temp.message_type, temp.pid
