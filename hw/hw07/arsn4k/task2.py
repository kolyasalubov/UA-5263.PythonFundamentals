from math import sqrt
from math import pi

def calculate_area_of_rectangle(side1: float, side2: float) -> float:
    """This function calculates an area of a rectangle.
    
    Args:
    side1: first side of a rectangle.
    side2: second of the sides of a rectangle.
    
    Returns: The area of the rectangle
    """
    result = side1 * side2
    return round(result, 3)

def calculate_area_of_triangle(side1: float, side2: float, side3: float) -> float:
    """
    This functions calculates an area of a triangle using Heron's formula.

    Args:
    side1: first side of a triangle.
    side2: second side of a triangle.
    side3: third side of a triangle.
    
    Returns: The area of the triangle
    """

    half_perimeter = (side1 + side2 + side3) / 2
    result = sqrt(half_perimeter * (half_perimeter - side1)
     * (half_perimeter - side2) * (half_perimeter - side3))
    return round(result, 3)

def calculate_area_of_circle(radius: float) -> float:
    """
    This function calculates an area of a circle.
    
    Args:
    radius: Radius of a circle.
    
    Returns:
    The area of the circle
    """
    
    result = pi * radius ** 2
    return round(result, 3)

def show_menu():
    """
    This function shows menu with 3 options.

    Returns: user's choice.
    """
    print("1. Calculate the area of a rectangle.")
    print("2. Calculate the area of a triangle.")
    print("3. Calculate the area of a circle.")

    user_choice = float(input())
    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please try again.")
        return show_menu()
    return user_choice


def main():
    """
    This function operates other functions and lets user enter sides
    """
    choice = show_menu()

    if choice == 1:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        print(f"Area = {calculate_area_of_rectangle(width, height)}")
    elif choice == 2:
        side_a = float(input("Enter side A: "))
        side_b = float(input("Enter side B: "))
        side_c = float(input("Enter side C: "))
        print(f"Area = {calculate_area_of_triangle(side_a, side_b, side_c)}")
    elif choice == 3:
        radius = float(input("Enter radius: "))
        print(f"Area = {calculate_area_of_circle(radius)}")
    else:
        print("Wrong choice")

main()
