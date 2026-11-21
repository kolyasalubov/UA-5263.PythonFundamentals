from collections import Counter

class Polygon:
    def __init__(self, sides : list[float]):
        for side in sides:
            if type(side) != float and type(side) != int:
                raise TypeError("All sides must be a float or int")
            if side <= 0:
                raise ValueError("All sides should have positive length number")
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, sides: list[float]):
        super().__init__(sides)
        if len(sides) != 4:
            raise ValueError("This is not rectangle")

        self.checkSides()

    def checkSides(self):
        if sorted(Counter(self.sides).values()) not in ([2, 2], [4]):
            raise ValueError("This is not rectangle")

    def findSquare(self):
        return max(self.sides) * min(self.sides)


print(Rectangle([10, 5, 10, 5]).findSquare())