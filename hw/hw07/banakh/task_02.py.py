import math


def get_rectangle_area(length, width):
    """Обчислює площу прямокутника."""
    return length * width


def get_triangle_area(base, height):
    """Обчислює площу трикутника."""
    return 0.5 * base * height


def get_circle_area(radius):
    """Обчислює площу кола."""
    return math.pi * (radius ** 2)


def main():
    print("Оберіть фігуру: 1 - прямокутник, 2 - трикутник, 3 - коло")
    choice = input("Ваш вибір: ")

    if choice == "1":
        a = float(input("Введіть довжину: "))
        b = float(input("Введіть ширину: "))
        print("Площа:", get_rectangle_area(a, b))
    elif choice == "2":
        a = float(input("Введіть основу: "))
        h = float(input("Введіть висоту: "))
        print("Площа:", get_triangle_area(a, h))
    elif choice == "3":
        r = float(input("Введіть радіус: "))
        print("Площа:", get_circle_area(r))
    else:
        print("Помилка: потрібно ввести 1, 2 або 3.")


if __name__ == "__main__":
    main()