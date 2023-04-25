import logging
import sys
from datetime import datetime


formatter = logging.Formatter("%(levelname)s: %(message)s")

std_err_handler = logging.StreamHandler(sys.stdout)
std_err_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(std_err_handler)
logger.setLevel(logging.DEBUG)

log_levels = {
    logging.DEBUG: logger.debug,
    logging.INFO: logger.info,
    logging.WARNING: logger.warning,
    logging.ERROR: logger.error,
    logging.CRITICAL: logger.critical
}


def log(level: logging.DEBUG | logging.INFO | logging.WARNING | logging.ERROR | logging.CRITICAL):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name = func.__name__
            time_called = datetime.now()
            func_return_value = func(*args, **kwargs)
            time_done = datetime.now()

            log_levels[level](f"Call time: {time_called.time()}; Duration time: {time_done - time_called}; "
                              f"Function name: {name}; Args: {args}; Kwargs: {kwargs}; "
                              f"Returned value: {func_return_value}")

            return func_return_value

        return wrapper

    return decorator


@log(logging.DEBUG)
def some_fun(a, b, c):
    return a + b + c


if __name__ == "__main__":
    some_fun(2, 3, 4)
