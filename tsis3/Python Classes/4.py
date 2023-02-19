class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, other_point):
        return abs((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

point1 = Point(2, 6)
point1.show()

point1.move(0, -2)
point1.show()

point2 = Point(0, 0)
point2.show()

print(point1.dist(point2))
