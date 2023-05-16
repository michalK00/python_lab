from SSHLogFactory import SSHLogFactory
from SSHLogEntry import SSHLogEntry
from datetime import datetime
from ipaddress import IPv4Address, ip_address, IPv6Address
import pytest


def test_get_date() -> None:
    # given
    datetime_object: datetime = datetime.strptime(
        "10/12/2023 07:02:47", "%d/%m/%Y %H:%M:%S"
    )
    raw_log: str = "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"

    # when
    log: SSHLogEntry = SSHLogFactory.get_log_entry(raw_log)
    # then
    assert log.date == datetime_object


def test_get_ipv4_correct() -> None:
    # given
    ip_v4: IPv4Address | IPv6Address = ip_address("212.47.254.145")
    raw_log: str = "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"
    # when
    log: SSHLogEntry = SSHLogFactory.get_log_entry(raw_log)
    # then
    assert log.ip_v4 == ip_v4


def test_get_ipv4_incorrect() -> None:
    # given
    ip_v4: IPv4Address | None = None
    raw_log: str = "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 666.777.88.213 [preauth]"
    # when
    log: SSHLogEntry = SSHLogFactory.get_log_entry(raw_log)
    # then
    assert log.ip_v4 == ip_v4

    # or
    # with pytest.raises(ValueError) as excinfo:
    #     SSHLogFactory.get_log_entry(raw_log)
    # assert "Invalid ip address!" in str(excinfo.value)

    # but then we need to raise an exception in SSHLogEntry.get_ipv4s_from_log, not catch it


def test_get_ipv4_empty() -> None:
    # given
    ip_v4: IPv4Address | None = None
    raw_log: str = "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed [preauth]"
    # when
    log: SSHLogEntry = SSHLogFactory.get_log_entry(raw_log)
    # then
    assert log.ip_v4 == ip_v4
