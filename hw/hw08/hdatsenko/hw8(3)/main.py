import calculate

import calculate


def main():
    shape = input("Enter the shape (triangle, rectangle, circle): ").strip().lower()
    if shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))  # Добавили ввод высоты
        area = calculate.calculate_area(shape, base, height)
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate.calculate_area(shape, length, width)
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = calculate.calculate_area(shape, radius)
    else:
        print("Unsupported shape.")
        return

    print(f"The area of the {shape} is: {area}")


if __name__ == "__main__":
    main()
