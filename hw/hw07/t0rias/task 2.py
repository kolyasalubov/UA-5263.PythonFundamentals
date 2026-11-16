import math

def rectangle_area(width, height):
    """
    Return the area of a rectangle.
    """
    return width * height

def triangle_area(base, height):
    """
    Return the area of a triangle.
    """
    return 0.5 * base * height

def circle_area(radius):
    """
    Return the area of a circle.
    """
    return math.pi * radius ** 2

print("Choose a shape:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")
choice = input("Your choice: ")

if choice == "1":
    width = float(input("Width: "))
    height = float(input("Height: "))
    print("Area:", rectangle_area(width, height))
elif choice == "2":
    base = float(input("Base: "))
    height = float(input("Height: "))
    print("Area:", triangle_area(base, height))
elif choice == "3":
    radius = float(input("Radius: "))
    print("Area:", round(circle_area(radius), 2))
else:
    print("Unknown choice")