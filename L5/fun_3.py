import logging
import sys

from type_enum import TypeOfMessage as msg

# {line, type, date, source, message}
formatter = logging.Formatter("%(levelname)s: %(message)s")

std_out_handler = logging.StreamHandler(sys.stdout)
std_out_handler.setLevel(logging.DEBUG)
std_out_handler.setFormatter(formatter)
std_out_handler.addFilter(lambda some_log: some_log.levelno <= logging.WARNING)

std_err_handler = logging.StreamHandler(sys.stderr)
std_err_handler.setLevel(logging.ERROR)
std_err_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(std_out_handler)
logger.addHandler(std_err_handler)


def change_min_logging_level(type_of_log):
    logger.setLevel(type_of_log)


def read_bytes_of_log(log):
    bytes_of_message = len(log.get("message").encode("utf-8"))  # in python 1 byte per char
    logger.debug("Line number " +
                 str(log.get("line")) +
                 ", bytes: " +
                 str(bytes_of_message))


def check_message_type(log):
    read_bytes_of_log(log)
    match log.get("type"):
        case msg.LOGIN_SUCCESSFUL | msg.CONNECTION_CLOSED:
            logger.info(log.get("message"))
        case msg.LOGIN_FAILURE:
            logger.warning(log.get("message"))
        case msg.WRONG_USER | msg.WRONG_PASSWORD:
            logger.error(log.get("message"))
        case msg.BREAK_IN_ATTEMPT:
            logger.critical(log.get("message"))


if __name__ == "__main__":
    log_4_testing = {"line": 1, "type": msg.BREAK_IN_ATTEMPT, "date": "Dec 10 06:55:46",
                     "source": " LabSZ sshd[24200]",
                     "message": "Invalid user webmaster from 173.234.31.186"}

    change_min_logging_level(logging.DEBUG)
    check_message_type(log_4_testing)
    logger.debug("DEBUG1")
    logger.info("INFO1")
    logger.warning("WARNING1")
    logger.error("ERROR1")
    logger.critical("CRITICAL1")
