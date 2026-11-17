import math


def calc_rectangle_area(a: float, b: float) -> float:
    return a * b


def calc_triangle_area(height: float, base: float) -> float:
    return 0.5 * height * base


def calc_circle_area(radius: float) -> float:
    return math.pow(radius, 2) * math.pi
