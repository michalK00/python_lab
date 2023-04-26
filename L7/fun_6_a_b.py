import logging
import sys
from datetime import datetime
from time import sleep

formatter = logging.Formatter("%(levelname)s: %(message)s")

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

log_levels = {
    logging.DEBUG: logger.debug,
    logging.INFO: logger.info,
    logging.WARNING: logger.warning,
    logging.ERROR: logger.error,
    logging.CRITICAL: logger.critical
}


def log(level):
    if level not in log_levels.keys():
        raise TypeError(f"Incorrect parameter: {level}")

    def decorator(decorated):
        def wrapper(*args, **kwargs):
            time_called = datetime.now()
            call_of_decorated = decorated(*args, **kwargs)
            time_done = datetime.now()
            # checks whether "decorated" argument is a class
            if isinstance(decorated, type):
                # if is class
                log_levels[level](f"Creation time: {time_called.time()}; "
                                  f"Class name: {decorated.__name__}; Constructor args: {args} and kwargs: {kwargs}")
            else:
                # if isn't class
                log_levels[level](f"Call time: {time_called.time()}; Duration time: {time_done - time_called}; "
                                  f"Function name: {decorated.__name__}; Args: {args} and kwargs: {kwargs}; "
                                  f"Returned value: {call_of_decorated}")

            return call_of_decorated

        return wrapper

    return decorator


@log(logging.DEBUG)
def some_fun(a, b, c):
    sleep(1)
    return a + b + c


@log(logging.INFO)
class SomeClass:
    def __init__(self, name):
        self.name = name
        print(f"{type(self).__name__} named {self.name} is created!")

    def show_that_you_are_alive(self):
        print(f"{type(self).__name__} named {self.name} is alive!")


if __name__ == "__main__":
    instance = SomeClass("Peter")
    instance.show_that_you_are_alive()

    some_fun(1, 2, 3)
