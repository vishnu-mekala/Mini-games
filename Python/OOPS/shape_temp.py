from math import sqrt
from math import pi

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  
    def area(self):
        print(f'\nThe area of the circle of radius {self.radius} is {pi*(self.radius**2)}')
    def perimeter(self):
        print(f'The perimeter of circle of radius {self.radius} is {2* pi * self.radius}\n')

class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)
    def area(self):
        print(f'\nThe surface area of the sphere of radius {self.radius} is {(4 * pi * (self.radius ** 2))}')
    def volume(self):
        print(f'The volume of the sphere of radius {self.radius} is {(4/3) * pi * (self.radius ** 3)}\n')

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f'\nThe area of the rectangle is {self.length * self.breadth}')
    def perimeter(self):
        print(f'The perimeter of rectangle is {2 * (self.length + self.breadth)}\n')

class Cuboid(Rectangle):
    def __init__(self, length, breadth, width):
        super().__init__(length,breadth)
        self.width = width
    def area(self):
        s_area = (2*self.length*self.breadth)+(2*self.length*self.width)+(2*self.breadth*self.width)
        print(f'\nThe surface area of the cuboid is {s_area}')
    def volume(self):
        print(f'The volume of the cuboid is {self.length*self.breadth*self.width}\n')

class Triangle(Shape):
    def __init__(self, side1, side2, side3, height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        
    def area(self):
        print(f'\nThe area of the triangle is {(1/2)*self.side1*self.height}')
    def perimeter(self):
        perimeter = self.side1+self.side2+self.side3
        print(f'The perimeter of the triangle is {perimeter}\n')

class Cone():
    def __init__(self,radius, height):
        self.radius = radius
        self.height = height
    def area(self):
        area = pi*self.radius*(pi + sqrt(self.height**2)+(self.radius**2))
        print(f'\nThe surface area of the cone is {area}')
    def volume(self):
        print(f'The volume of cone is {pi*(self.radius ** 2)*(self.height/3)}\n')

circle = Circle(5)
circle.area()
circle.perimeter()

sphere = Sphere(5)
sphere.area()
sphere.volume()

cube = Cuboid(4,5,6)
cube.area()
cube.volume()

rect = Rectangle(4,5)
rect.area()
rect.perimeter()

cone = Cone(4,7)
cone.area()
cone.volume()

tri = Triangle(4,5,6,7)
tri.area()
tri.perimeter()