class Shape:
    def area(self):
        return 0 
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
class Cube(Square):
    def volume(self):
        return self.length ** 3
    
def func1(p1, p2, p3):
    pass

func1(p1, p2, p3)

a:n = lambda a, n : a**n
