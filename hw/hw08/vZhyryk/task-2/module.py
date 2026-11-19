import math

def calc_rectangle_area(a : float, b : float) -> float:
       return round(a * b, 2)

def calc_triangle_area(base : float, height : float) -> float:
       return round(0.5 * base * height, 2)

def calc_circle_area(r : float) -> float:
       return round(math.pow(r, 2) * math.pi, 2)

