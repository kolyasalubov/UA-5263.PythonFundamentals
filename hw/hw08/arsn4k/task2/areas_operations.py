from math import pi

def calculate_area_of_rectangle(side_a: float, side_b: float) -> float:
    """This function calculates an area of a rectangle.
    
    Args:
        side_a: first side of a rectangle.
        side_b: second side of a rectangle.
    
    Returns: The area of the rectangle
    """
    result = side_a * side_b
    return round(result, 3)

def calculate_area_of_triangle(height: float, side_a: float) -> float:
    """
    This functions calculates an area of a triangle using the base and height.

    Args:
        height: height of the triangle.
        side_a: base of the triangle.

    Returns:
        The area of the triangle
    """
    result = 0.5 * height * side_a
    return round(result, 3)

def calculate_area_of_circle(radius: float) -> float:
    """
    This function calculates an area of a circle.
    
    Args:
    radius: Radius of a circle.
    
    Returns:
    The area of the circle
    """
    
    result = pi * pow(radius, 2)
    return round(result, 3)
