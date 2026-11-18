def count_characters(word):  
    """
    Calculates the occurrences of each character
    in  a given string.

    Args:
    word (str): The input string.

    Returns:
    dict: A dictionary with characters as keys
    and their occurrence counts as values.
    """
    characters = {}
    for letter in word:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters


print(count_characters("hello"))
