def count_special_numbers() -> int:

    """
    Counts natural numbers on [a; b] that are not divisible by c
    and end with digit d.
    Returns:
        int: count of such numbers.
    """

    a, b, c, d = map(int, input().split())
    numbers = range(a, b + 1)
    count = map(lambda x: 1 if x % c != 0 and x % 10 == d else 0, numbers)
    return sum(count)


if __name__ == "__main__":
    print(count_special_numbers())
