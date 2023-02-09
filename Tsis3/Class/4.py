import math

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point {}, {}".format(self.x, self.y))

    def move(self, x, y):
        self.x = x
        self.y = y
        print("New point {}, {}".format(self.x, self.y))


    def dict(self, x,y):
        a = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        print(a)

x = int(input())
x1 = int(input())
y = int(input())
y1 = int(input())

s = Point(x, y)
s.show()
s.move(x1, y1)
s.dict(x, y)





