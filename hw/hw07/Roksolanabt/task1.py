def max_of_two(a, b):
    """Return the larger of two numbers.
    If the numbers are equal, returns either of them.
    """
    if a > b:
        return a
    return b


if __name__ == "__main__":
    x = float(input("First number: "))
    y = float(input("Second number: "))
    print("Max:", max_of_two(x, y))
