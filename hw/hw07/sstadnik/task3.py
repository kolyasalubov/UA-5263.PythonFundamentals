def character_count(text):
    """
    Return how many times each character appears in a string.

    Args:
        text: The string to count characters in.

    Returns:
        A dictionary where each key is a character and each value is its count.
    """
    return {character: text.count(character) for character in text}

print(character_count('hello'))
