import logging
import sys

from type_enum import TypeOfMessage

# {line, type, date, source, message}
formatter = logging.Formatter("%(levelname)s:%(message)s")

std_out_handler = logging.StreamHandler(sys.stdout)
std_out_handler.setLevel(logging.DEBUG)
std_out_handler.setFormatter(formatter)
std_out_handler.addFilter(lambda some_log: some_log.levelno <= logging.WARNING)

std_err_handler = logging.StreamHandler(sys.stderr)
std_err_handler.setLevel(logging.ERROR)
std_err_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(std_out_handler)
logger.addHandler(std_err_handler)


def check_message_type(log):
    read_bytes_of_log(log)
    match log.get("type"):
        case TypeOfMessage.LOGIN_OR_DISCONNECT_SUCCESS:
            logger.info(log.get("message"))
        case TypeOfMessage.LOGIN_FAILURE:
            logger.warning(log.get("message"))
        case TypeOfMessage.ERROR:
            logger.error(log.get("message"))
        case TypeOfMessage.HACK_ATTEMPT:
            logger.critical(log.get("message"))


def read_bytes_of_log(log):
    bytes_of_message = len(log.get("message").encode("utf-8"))  # in python 1 byte per char
    logger.debug("Line number " +
                 str(log.get("line")) +
                 ", bytes: " +
                 str(bytes_of_message))


if __name__ == "__main__":
    log_4_testing = {"line": 1, "type": TypeOfMessage.LOGIN_OR_DISCONNECT_SUCCESS, "date": "Dec 10 06:55:46",
                     "source": " LabSZ sshd[24200]",
                     "message": "Invalid user webmaster from 173.234.31.186"}

    # check_message_type(log_4_testing)
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("WARNING")
    logger.error("ERROR")
    logger.critical("CRITICAL")
