import math


def get_rectangle_area(a: float, b: float) -> float:
    return a * b


def get_triangle_area(base: float, height: float) -> float:
    return base * height / 2


def get_circle_area(radius: float) -> float:
    return math.pi * radius**2


def main() -> None:
    choice = input("Enter shape (rectangle/triangle/circle): ").strip().lower()

    if choice == "rectangle":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        area = get_rectangle_area(a, b)
    elif choice == "triangle":
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = get_triangle_area(base, height)
    elif choice == "circle":
        radius = float(input("Radius: "))
        area = get_circle_area(radius)
    else:
        print("Unknown shape. Choose rectangle, triangle, or circle.")
        return

    print(f"Area: {area}")


if __name__ == "__main__":
    main()
