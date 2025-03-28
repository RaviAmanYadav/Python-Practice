import time


def timer(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        print(f"{func.__name__} ran in {endTime - startTime} seconds")
        return result

    return wrapper


@timer
def exampleFunctin(n):
    time.sleep(n)


exampleFunctin(2)
