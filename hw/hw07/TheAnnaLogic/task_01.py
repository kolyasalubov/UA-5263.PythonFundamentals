def return_largest_number(num1, num2):
    """
    This function returns the largest number among the two given numbers
    input parameters: num1 - int, num2 - int
    output: int
    """
    if num1 < num2:
        return num2
    return num1


print(return_largest_number(12, 16))
