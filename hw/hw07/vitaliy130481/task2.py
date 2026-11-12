import math
def get_rectangle_area(a, b):
    return a * b

def get_triangle_area(a, h):
    return 0.5 * a * h

def get_circle_area(r):
    return math.pi * (r ** 2)

choice = input("Enter shape (rectangle/triangle/circle): ").strip().lower()

if choice == "rectangle":
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    print(get_rectangle_area(a, b))
elif choice == "triangle":
    a = float(input("Base: "))
    h = float(input("Height: "))
    print(get_triangle_area(a, h))
elif choice == "circle":
    r = float(input("Radius: "))
    print(get_circle_area(r))