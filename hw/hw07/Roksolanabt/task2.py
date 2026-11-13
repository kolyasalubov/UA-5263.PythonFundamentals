import math

def rectangle_area(width, height):
    return width * height


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * radius ** 2


def main():
    print("1 - rectangle")
    print("2 - triangle")
    print("3 - circle")
    choice = input("Choose a shape: ")

    match choice:
        case "1":
            w = float(input("Width: "))
            h = float(input("Height: "))
            area = rectangle_area(w, h)
        case "2":
            b = float(input("Base: "))
            h = float(input("Height: "))
            area = triangle_area(b, h)
        case "3":
            r = float(input("Radius: "))
            area = circle_area(r)
        case _:
            print("Wrong choice")
            return

    print(f"Area = {area}")


if __name__ == "__main__":
    main()