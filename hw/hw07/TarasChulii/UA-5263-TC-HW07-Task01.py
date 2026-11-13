def return_largest_number(num1: int, num2: int) -> int:
    """This function returns largest number from two whole numbers."""
    #Option#1
    if num1 >= num2:
        return num1
    return num2
    #Option#2
    #return max(num1, num2)


print(return_largest_number.__doc__)
print(return_largest_number(1, 9))
print(return_largest_number(-9, 1))
print(return_largest_number(8, 8))