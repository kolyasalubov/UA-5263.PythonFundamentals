def calculate_number_of_characters(word: str) -> dict:
    """This function calculates amount of entries for each characters included in given string."""
    
    result = {}
    
    for char in word.lower():
        result[char] = result.get(char, 0) + 1
            
    return result


def self_test():
    
    print(calculate_number_of_characters.__doc__)
    print(calculate_number_of_characters("abcbca"))
    print(calculate_number_of_characters("aaAabbbBBbbwwwwWWww"))
    print(calculate_number_of_characters("hello"))


if __name__ == "__main__":
    self_test()