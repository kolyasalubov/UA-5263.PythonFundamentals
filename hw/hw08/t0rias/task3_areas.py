from math import pow, pi
"""
This module includes functions to calculate the area of different shapes.
"""

def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height

def triangle_area(base, height):
    """Return the area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Return the area of a circle."""
    return pi * pow(radius, 2)