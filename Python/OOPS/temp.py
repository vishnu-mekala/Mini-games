from ast import Return
from math import pi

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return (self.radius**2)*pi
    
    def perimeter(self):
        return 2*self.radius*pi

class Sphere(Circle):
    def __init__(self, r):
        super().__init__(r)
    def area(self):
        return 4 * pi * (self.r ** 2)

obj = Sphere(Circle(10))
print(obj.area())