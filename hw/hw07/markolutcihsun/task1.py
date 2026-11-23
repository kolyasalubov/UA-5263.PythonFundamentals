def find_max(a, b):
    """Повертає найбільше з двох переданих чисел."""
    if a > b:
        return a
    return b


result = find_max(1, 5)
print(f"Найбільше число: {result}")