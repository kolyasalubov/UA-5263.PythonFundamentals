import math
import random
import re


class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

    @property
    def ballType(self):
        return self.ball_type


class Ghost:
    def __init__(self):
        self.color = random.choice(("white", "yellow", "purple", "red"))


class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


class God:
    @staticmethod
    def create():
        return [Man(), Woman()]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round((4 / 3) * math.pi * self.radius**3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)

    def get_density(self):
        return round(self.mass / ((4 / 3) * math.pi * self.radius**3), 5)


def class_name_changer(cls, new_name):
    if not isinstance(new_name, str) or re.fullmatch(r"[A-Z][A-Za-z0-9]*", new_name) is None:
        raise ValueError("Class names must start with a capital letter and contain only letters and digits.")
    cls.__name__ = new_name
