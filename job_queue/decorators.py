# @retry, @log, @timeit
import logging
import time, datetime

LOG_FILE = "../logs/jobs.log"

# This has setup global things
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def retry(max_retry = 4, delay_time = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attemps = 0
            while attemps < max_retry:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Function {func.__name__}, Error={e}, args={kwargs}, kwargs={kwargs}, retrying attemps...{attemps + 1}")
                    logging.error(f"Function {func.__name__}, Error={e}, args={kwargs}, kwargs={kwargs}, retrying attempts...{attemps + 1}")
                    attemps += 1
                    time.sleep(delay_time)
            return
        return wrapper
    return decorator

def log(func):
    """This opens a file and logs in and then closes the file"""
    def wrapper(*args, **kwargs):
        logging.info(f"Started function {func.__name__}, args={args}, kwargs={kwargs}")
        try:
            results = func(*args, **kwargs)
            logging.info(f"Function {func.__name__} finished and gave output of {results}")
            return results
        except Exception as e:
            logging.error(f"Function {func.__name__} got error: {e}")
    return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        results = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"The function took {duration:.2f} s")
        return results
    return wrapper