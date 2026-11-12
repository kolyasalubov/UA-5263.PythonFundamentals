def largest_number(first, second):
    """
    Return the largest of two numbers.

    Args:
        first: The first number.
        second: The second number.

    Returns:
        The larger of the two numbers. If they are equal, returns that value.
    """
    if first >= second:
        return first
    return second



print(largest_number(8, 3))
print(largest_number(2, 10))
