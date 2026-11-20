import areas


def main() -> None:
    shape = input("Which shape (rectangle/triangle/circle)? ").strip().lower()

    if shape == "rectangle":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        area = areas.calc_rectangle_area(a, b)
    elif shape == "triangle":
        height = float(input("Height: "))
        base = float(input("Base: "))
        area = areas.calc_triangle_area(height, base)
    elif shape == "circle":
        radius = float(input("Radius: "))
        area = areas.calc_circle_area(radius)
    else:
        print("Unknown shape. Choose rectangle, triangle, or circle.")
        return

    print(f"Area: {area}")


if __name__ == "__main__":
    main()
