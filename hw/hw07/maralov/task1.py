def max_of_two(a, b):
    """
    Повертає більше з двох чисел.
    """
    if a > b:
        return a
    else:
        return b


print(max_of_two(3, 7))      # 7
print(max_of_two(10, -2))    # 10
print(max_of_two(2.5, 2.5))  # 2.5
print(max_of_two.__doc__)
