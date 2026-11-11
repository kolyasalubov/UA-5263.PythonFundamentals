def calc_triangle_area(base: int, high: int) -> float:
    return base * high * 0.5


def calc_rectangle_area(a : int, b: int) -> int:
    return a * b

def calc_circle_area(r : int) -> float:
    return 3.14 * r**2

def calc_area(figure : str):
    match figure:
        case "triangle":
            print(calc_triangle_area(5,5))
        case "rectangle":
            print(calc_rectangle_area(5,5))
        case "circle":
            print(calc_circle_area(5))
        case _:
            print("invalid figure")


val = input()

calc_area(val)