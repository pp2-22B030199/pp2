class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

s = Shape()
print(s.area())

a = float(input())
s1 = Square(a)

print(s1.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

b = Rectangle(int(input()), int(input()))
print(b.area())