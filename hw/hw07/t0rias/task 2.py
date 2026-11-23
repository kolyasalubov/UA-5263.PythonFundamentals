import math

def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height

def triangle_area(base, height):
    """Return the area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2

def read_positive_number(prompt):
    """
    Ask the user for a number until a positive value is entered.
    """
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if value <= 0:
            print("The value must be greater than zero.")
            continue
        return value

def main():
    print("Choose a shape:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")
    choice = input("Your choice: ").strip()

    if choice == "1":
        width = read_positive_number("Width: ")
        height = read_positive_number("Height: ")
        area = rectangle_area(width, height)
    elif choice == "2":
        base = read_positive_number("Base: ")
        height = read_positive_number("Height: ")
        area = triangle_area(base, height)
    elif choice == "3":
        radius = read_positive_number("Radius: ")
        area = circle_area(radius)
    else:
        print("Unknown choice")
        return

    print("Area:", round(area, 2))

if __name__ == "__main__":
    main()