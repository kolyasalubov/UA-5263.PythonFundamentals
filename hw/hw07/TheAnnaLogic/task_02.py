import math

def rectangle_area(a, b):
    """
    Calculate the area of a rectangle.
    Parameters:
    a (float): The length of the rectangle.
    b (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return a * b


def circle_area(r):
    """
    Calculate the area of a circle.
    Parameters:
    r (float): The radius of the circle.
    Returns:
    float: The area of the circle.
    """
    return math.pi * r ** 2


def triangle_area(a, h):
    """
    Calculate the area of a triangle.
    Parameters:
    a (float): The base of the triangle.
    h (float): The height of the triangle.
    Returns:
    float: The area of the triangle.
    """
    return 0.5 * a * h
 
 
choice = input("Enter your choice: 1 - Rectangle, 2 - Circle, 3 - Triangle: ")
if choice == '1':
    a = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(a, b)
    print(f"The area of the rectangle is: {area}")
elif choice == '2':
    r = float(input("Enter the radius of the circle: "))
    area = circle_area(r)
    print(f"The area of the circle is: {area}")
elif choice == '3':
    a = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = triangle_area(a, h)
    print(f"The area of the triangle is: {area}")

else:
    print("Invalid choice")
    