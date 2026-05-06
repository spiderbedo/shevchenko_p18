def print_result(func):
  
    """
    Decorator that prints the result of a one-argument function.
    """
  
    def wrapper(x):
        result = func(x)
        print(result)
        return result
    return wrapper


@print_result
def square(x) -> int:
    return x * x


if __name__ == "__main__":
    n = int(input())
    square(n)
