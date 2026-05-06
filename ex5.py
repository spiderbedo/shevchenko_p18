from functools import reduce

def product_squares() -> int:

    """
    Finds the product of natural numbers on [a; b] that are perfect squares
    and are divisible by c.
    Returns:
        int: product of suitable numbers.
    """
    a, b, c = map(int, input().split())
    numbers = range(a, b + 1)
    filtered = filter(lambda x: int(x ** 0.5) ** 2 == x and x % c == 0, numbers)
    return reduce(lambda x, y: x * y, filtered, 1)


if __name__ == "__main__":
    print(product_squares())
