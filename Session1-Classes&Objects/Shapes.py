
class Shape:

    def __init__(self, name):
        self.name = name

    def perimeter(self):
        raise NotImplementedError("cannot computer perimeter")
    
    def area(self):
        raise NotImplementedError("cannot computer area")
        

s = Shape("generic shape")
print(s.name)
print(s.area)
