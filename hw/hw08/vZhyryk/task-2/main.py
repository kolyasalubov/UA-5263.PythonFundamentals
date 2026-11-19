import module

try:
    a = float(input("Rectangle side a: "))
    b = float(input("Rectangle side b: "))
    print("calc_rectangle_area:", module.calc_rectangle_area(a, b))
except ValueError:
    print("a and b must be float")

try:
    base = float(input("Triangle base: "))
    h = float(input("Triangle height: "))
    print("calc_triangle_area:", module.calc_triangle_area(base, h))
except ValueError:
    print("base and height must be float")

try:
    r = float(input("Circle radius: "))
    print("calc_circle_area:", module.calc_circle_area(r))
except ValueError:
    print("radius must be float")