def count_uppercase() -> int:
    """
    Counts uppercase letters in srez from i to j
    Returns:
        int: number of uppercase letters
    """
    s = input().strip()
    i, j = map(int, input().split())
    srez = s[i-1:j]
    result = list(filter(lambda x: x.isupper(), srez)
    return len(result)


if __name__ == "__main__":
    print(count_uppercase())
