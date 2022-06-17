from math import pi
from operator import length_hint
class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.radius**2*pi
    
    def perimeter(self):
        return 2*self.radius*pi