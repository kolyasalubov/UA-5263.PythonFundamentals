def count_characters(text):
    """Рахує кількість кожного символу в рядку."""
    result_dict = {}
    for letter in text:
        if letter in result_dict:
            result_dict[letter] = result_dict[letter] + 1
        else:
            result_dict[letter] = 1
    return result_dict