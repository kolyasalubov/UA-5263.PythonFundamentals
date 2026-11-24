#I. Ball-super-ball
class Ball():
    # your code goes here
    def __init__(self, ball_type = 'regular'):
        self.ball_type = ball_type


#II. Color-ghost
import random

class Ghost():
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


#III. Basic-subclasses-Adam-and-Eve
class Human():
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


#IV. Classy-classes
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if int(age) <=0:
            raise ValueError("Incorrect age, age should be greter than 0")
        self._age = int(age)
        
    @property   
    def info(self):
        return f"{self.name}s age is {self.age}"


#V. Building Spheres
import math

class Sphere():
    
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4 / 3 * math.pi * pow(self.radius, 3), 5)
    
    def get_surface_area(self):
        return round(4 * math.pi * pow(self.radius, 2), 5)
    
    def get_density(self):
        return round(self.mass/ (4 / 3 * math.pi * pow(self.radius, 3)), 5)


#VI. Dynamic Classes
def class_name_changer(cls, new_name):
    
    if not new_name or not new_name[0].isupper() or not new_name.isalnum():
        raise Exception("Name of new class is invalid")
        
    cls.__name__ = new_name