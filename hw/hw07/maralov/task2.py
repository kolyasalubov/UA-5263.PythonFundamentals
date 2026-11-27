import math


def rectangle_area(a, b):
    """Повертає площу прямокутника зі сторонами a і b."""
    return a * b


def triangle_area(base, height):
    """Повертає площу трикутника за основою і висотою."""
    return 0.5 * base * height


def circle_area(radius):
    """Повертає площу кола за радіусом."""
    return math.pi * radius ** 2


def main():
    print("Оберіть фігуру:")
    print("1 - прямокутник")
    print("2 - трикутник")
    print("3 - коло")
    choice = input("Ваш вибір (1/2/3): ")

    if choice == "1":
        a = float(input("Введіть першу сторону: "))
        b = float(input("Введіть другу сторону: "))
        print(f"Площа прямокутника: {rectangle_area(a, b)}")
    elif choice == "2":
        base = float(input("Введіть основу: "))
        height = float(input("Введіть висоту: "))
        print(f"Площа трикутника: {triangle_area(base, height)}")
    elif choice == "3":
        radius = float(input("Введіть радіус: "))
        print(f"Площа кола: {circle_area(radius):.2f}")
    else:
        print("Невірний вибір, введіть 1, 2 або 3")


if __name__ == "__main__":
    main()
