def calculate_number_of_chars(text: str) -> dict:
    """
    This function calculates the number of each character in a given string.

    Args:
    text: input text.

    Returns: dictionary, where keys are characters and values are counted numbers.
    """
    
    output_dict = {}

    for letter in text:
        output_dict[letter] = text.count(letter)
    
    return output_dict

input_text = input("Enter a string: ")
# input_text = "Hello"
print(calculate_number_of_chars(input_text))