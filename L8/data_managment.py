from typing import Generator, Tuple
from datetime import datetime
import ipaddress

from SSHLogFactory import SSHLogFactory
from type_enum import TypeOfMessage as Msg

_log_list = []
_filtered_log_list = []


# Generator[yield_type, send_type, return type]
def gather_logs(file_path: str) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            _log_list.append(SSHLogFactory.get_log_entry(line))


def get_logs() -> Generator[str, None, None]:
    for log in _log_list:
        yield log.entire_raw_log


def get_logs_between_dates(start_date: datetime, end_date: datetime) -> Generator[str, None, None]:
    _filtered_log_list.clear()
    for log in _log_list:
        if start_date <= log.date <= end_date:
            _filtered_log_list.append(log)
            yield log.entire_raw_log


def get_item_from_log_list(index: int) -> Tuple[datetime, str, ipaddress, Msg, int]:
    if 0 <= index < len(_log_list):
        temp = _log_list[index]
        return temp.date, temp.user, temp.ip_v4, temp.message_type, temp.pid


def get_item_from_filtered_list(index: int) -> Tuple[datetime, str, ipaddress, Msg, int]:
    if 0 <= index < len(_filtered_log_list):
        temp = _filtered_log_list[index]
        return temp.date, temp.user, temp.ip_v4, temp.message_type, temp.pid