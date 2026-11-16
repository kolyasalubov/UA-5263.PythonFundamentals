def count_chars(text):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result