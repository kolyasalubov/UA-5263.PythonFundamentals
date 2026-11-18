import math

def calculate_rectangle_area(length, width):
  return length * width

def calculate_triangle_area(base, height):
  return 0.5 * base * height

def calculate_circle_area(radius):
    pi = 3.14159
    return pi * (radius**2)


def main():
  print("Оберіть фігуру для обчислення площі:")
  print("1 - Прямокутник")
  print("2 - Трикутник")
  print("3 - Круг")

  choice = input("Введіть номер вибору 1, 2, 3: ")

  if choice == "1":
    length = float(input("Введіть довжину прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))
    area = calculate_rectangle_area(length, width)
    print(f"Площа прямокутника дорівнює: {area}")

  elif choice == "2":
    base = float(input("Введіть основу трикутника: "))
    height = float(input("Введіть висоту трикутника: "))
    area = calculate_triangle_area(base, height)
    print(f"Площа трикутника дорівнює: {area}")

  elif choice == "3":
    radius = float(input("Введіть радіус круга: "))
    area = calculate_circle_area(radius)
    print(f"Площа круга дорівнює: {area}")

  else:
    print("Помилка: вибрано неіснуючий пункт меню!")


if __name__ == "__main__":
    main()