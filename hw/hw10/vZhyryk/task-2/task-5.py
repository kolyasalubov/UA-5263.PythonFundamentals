from math import pi

class Sphere:
    def __init__(self, radius : int | float, mass : int | float):
        self.radius = radius
        self.mass = mass

    def get_radius(self) -> int | float:
        return self.radius

    def get_mass(self) -> int | float:
        return self.mass

    def get_volume(self) -> int | float:
        return 4 / 3 * pi * self.radius ** 3

    def get_surface_area(self) -> int | float:
        return 4 * pi * self.radius ** 2

    def get_density(self) -> int | float:
        return self.mass / self.get_volume()