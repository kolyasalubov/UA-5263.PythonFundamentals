import math
def rectangle_area(length: float, width: float) -> float:
    return length * width
def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height
def circle_area(radius: float) -> float:
    return math.pi * (radius ** 2)
def main():
    print("Виберіть фігуру для обчислення площі:")
    print("1 - Прямокутник")
    print("2 - Трикутник")
    print("3 - Коло")
    choice = input("Введіть номер (1, 2 або 3): ")
    if choice == '1':
        length = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        area = rectangle_area(length, width)
        print(f"Площа прямокутника: {area}")
    elif choice == '2':
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = triangle_area(base, height)
        print(f"Площа трикутника: {area}")
    elif choice == '3':
        radius = float(input("Введіть радіус кола: "))
        area = circle_area(radius)
        print(f"Площа кола: {area:.2f}")
    else:
        print("Помилка: вибрано невірний пункт меню!")
if __name__ == "__main__":
    main()