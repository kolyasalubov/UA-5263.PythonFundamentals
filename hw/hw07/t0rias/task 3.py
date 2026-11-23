def count_chars(text):
    """
    Count how many times each character occurs in a string.

    Args:
        text (str): Input string.

    Returns:
        dict: Characters as keys, their counts as values.
    """
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(count_chars("hello"))
print(count_chars(""))
print(count_chars("ellegance"))
print(count_chars("1111888889923"))