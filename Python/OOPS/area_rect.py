class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print(f'Area of Rectangle with {self.length=} & {self.breadth=} is {area}')

r = Rectangle(10, 20)
r.area()

r1 = Rectangle(100, 200)
r1.area()

r2 = Rectangle(17, 20)
r2.area()