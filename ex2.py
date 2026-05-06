def sum_multiples() -> int:
  
    """
    Finds the sum of numbers on [a; b] that are divisible by c and d.
    Returns:
        int: sum of suitable numbers.
    """
  
    a, b, c, d = map(int, input().split())
    numbers = range(a, b + 1)
    filtered = filter(lambda x: x % c == 0 and x % d == 0, numbers)
    return sum(filtered)


if __name__ == "__main__":
    print(sum_multiples())
