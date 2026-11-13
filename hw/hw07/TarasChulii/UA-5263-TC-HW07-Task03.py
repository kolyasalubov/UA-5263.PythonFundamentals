def calculate_number_of_characters(word: str) -> dict:
    """This function calculates amount of entries for each characters included in given string."""
    
    result = {}
    
    #Option#1
    #for char in word.lower():
    #   if char not in result:
    #       result[char] = 1
    #    else:
    #        result[char] += 1
          
    #Option#2
    for char in word.lower():
        result[char] = result.get(char, 0) + 1
            
    return result


print(calculate_number_of_characters.__doc__)
print(calculate_number_of_characters("abcbca"))
print(calculate_number_of_characters("aaAabbbBBbbwwwwWWww"))
print(calculate_number_of_characters("hello"))