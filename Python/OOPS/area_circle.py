import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius * self.radius
        print(f'Area of Circle with {self.radius=} is {area}')

r = Circle(22)
r.area()
