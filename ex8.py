import datetime

def log_exceptions(func):

    """
    Decorator that logs exceptions to a file.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open("log.txt", "a") as f:
                f.write(f"{datetime.datetime.now()} - {type(e).__name__}\n")
            raise
    return wrapper


@log_exceptions
def divide(a, b):
    return a / b


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(divide(x, y))
