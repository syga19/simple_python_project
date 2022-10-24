from typing import Callable, Optional
import logging
import time
logging.basicConfig(filename="output.log", level=logging.INFO)

def timer(fn: Callable) -> Callable:
    # TODO: Log how much time has passed
    def track_time(*args, **kwargs):
        start_time = time.time()
        rez = fn(*args, **kwargs)
        print(f"Execution time {time.time() - start_time}")
        return rez
    return track_time


#def calculator_logger(fn: Callable) -> Callable:
def calculator_logger(fn: Callable) -> Callable:
    # TODO: Log function name and it's args and kwargs
    def log_fn(*args, **kwargs):
        logging.info(f"Running a function {fn.__name__} with args {args} and {kwargs}")
        return fn(*args, **kwargs)
    return log_fn    


def input_parser(fn: Callable) -> Callable:
    def convert_to_int(*args) -> Optional[int]:
        # TODO: Enable this function to work with multiple args and kwargs
        try:
            return fn(args[0], int(args[1]))
        except Exception:
            print(f"Cannot convert input of type {type(args[1])} to an int")
            return None

    return convert_to_int
