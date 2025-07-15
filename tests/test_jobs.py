from job_queue.decorators import *
import random

class IntentionalError(Exception):
    pass

@log
def printName(name):
    raise IntentionalError('Raised an intentional error')
    return name

@retry(max_retry=6, delay_time=3)
def TrySomethingNew():
    random_number = random.random()
    print(f"Numberis: {random_number}")
    if random_number < 0.7:
        raise IntentionalError("Watmon Reagan Nyero")
    return "Hello"

if __name__ == "__main__":
    print(TrySomethingNew())