from math import pi

class Shape:

    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("cannot computer perimeter")
    
    def area(self):
        raise NotImplementedError("cannot computer area")

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius * self.radius
    

l = [Square("generic square", 10), Square("another square", 5), Circle("a circle", 3)]

for element in l:
    n = element.name
    p = element.perimeter()
    a = element.area()
    print(f"{n} has area {a} and perimeter {p}")

s = Square("generic square", 10)
print(s.perimeter())
print(s.area())

c = Circle("circle", 3)
print(c.perimeter())
print(c.area())
