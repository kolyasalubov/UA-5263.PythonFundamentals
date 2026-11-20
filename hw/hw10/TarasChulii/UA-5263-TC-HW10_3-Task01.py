class Polygon():
    def __init__(self, amount_of_sides):
        self.n = int(amount_of_sides)

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        return pow((p*(p-a)*(p-b)*(p-c)), 0.5)


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(int(self.n / 2))] * 2

    def findArea(self):
        a, b, *others = self.sides
        return a * b


def test_triangle():
    t = Triangle()
    t.inputSides()
    t.dispSides()
    print(f"The area of the triangle is {t.findArea():.2f}")

def test_rectangle():
    r = Rectangle()
    r.inputSides()
    r.dispSides()
    print(f"The area of the rectangle is {r.findArea():.2f}")


if __name__ == "__main__":
    test_triangle()
    test_rectangle()