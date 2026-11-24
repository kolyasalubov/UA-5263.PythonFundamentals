import math

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
        base, height = dimensions
        return 0.5 * base * height
    elif shape == 'rectangle':
        if len(dimensions) != 2:
            raise ValueError("Rectangle requires length and width.")
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        if len(dimensions) != 1:
            raise ValueError("Circle requires radius.")
        radius = dimensions[0]
        return math.pi * math.pow(radius, 2)
    else:
        raise ValueError("Unsupported shape. Supported shapes are: triangle, rectangle, circle.")