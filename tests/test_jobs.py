from job_queue.decorators import *

class IntentionalError(Exception):
    pass

@log
def printName(name):
    raise IntentionalError('Raised an intentional error')
    return name

if __name__ == "__main__":
    print(printName("Watmon Reagan"))