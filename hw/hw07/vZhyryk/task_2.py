def calc_triangle_area(base: int, high: int) -> float:
    return base * high * 0.5


def calc_rectangle_area(a : int, b: int) -> int:
    return a * b

def calc_circle_area(r : int) -> float:
    return 3.14 * r**2

def calc_area(figure: str, *vals: float) -> float | None:
    match figure:
        case "triangle":
            print(calc_triangle_area(*vals))
        case "rectangle":
            print(calc_rectangle_area(*vals))
        case "circle":
            print(calc_circle_area(*vals))
        case _:
            print("invalid figure")


if __name__ == "__main__":
    figure = input("Figure (triangle/rectangle/circle): ")
    values = [float(v) for v in input("Sizes (space separated): ").split()]
    calc_area(figure, *values)