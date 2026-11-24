def calculate_area_triangle(base, height):
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
    base (float): The length of the base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area
def calculate_area_rectangle(length, width):
    """
    Calculate the area of a rectangle given its length and width.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    area = length * width
    return area
def calculate_area_circle(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    import math
    area = math.pi * radius ** 2
    return area
def calculate_area(shape, *dimensions):
    """
    Calculate the area of a given shape based on its dimensions.

    Parameters:
    shape (str): The type of shape ('triangle', 'rectangle', 'circle').
    *dimensions: The dimensions required to calculate the area of the shape.

    Returns:
    float: The area of the shape.
    """
    if shape == 'triangle':
        if len(dimensions) != 2:
            raise ValueError("Triangle requires base and height.")
        return calculate_area_triangle(*dimensions)
    elif shape == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires length and width.")
        return calculate_area_rectangle(*dimensions)
    elif shape == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle requires radius.")
        return calculate_area_circle(*dimensions)
    else:
        raise ValueError("Unsupported shape type. Supported types are: triangle, rectangle, circle.")

print(calculate_area('triangle', 5, 10))  # Output: 25.0
    