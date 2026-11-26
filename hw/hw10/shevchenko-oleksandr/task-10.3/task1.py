class Polygon:
    def __init__(self, *sides):
        self.sides = tuple(float(side) for side in sides)

    def display_sides(self):
        for number, side in enumerate(self.sides, start=1):
            print(f"Side {number}: {side:g}")


class Rectangle(Polygon):
    def __init__(self, length, width):
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Rectangle sides must be positive numbers.")
        super().__init__(length, width, length, width)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def main():
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    rectangle = Rectangle(length, width)
    rectangle.display_sides()
    print(f"Rectangle area: {rectangle.area():g}")


if __name__ == "__main__":
    main()
