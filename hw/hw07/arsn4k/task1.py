def compare_two_numbers(num1: int, num2: int) -> int | str:
    """This functions returns larger number"""

    if num1 > num2:
        return num1
    elif num1 == num2:
        return "num1 = num2"
    return num2

print(compare_two_numbers.__doc__)
print(compare_two_numbers(120, 28))
print(compare_two_numbers(34,254))
print(compare_two_numbers(50,50))