def largest(a, b):
    """
    Return the largest number of two.
    
    Args:
        a (int | float): First number
        b (int | float): Second number

        Returns:
        int | float: The larger of a and b.
    """
    if a > b:
        return a
    return b

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print("The largest number is: ", largest(first, second))
print(largest.__doc__)