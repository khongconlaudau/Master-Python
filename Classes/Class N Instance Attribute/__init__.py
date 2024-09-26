class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point: {self.x}, {self.y}")

Point.default_color = "blue"  # change default color in the class

point1 = Point(1, 2)
point1.z = 10     # add attributes for object point but does not change anything in the class
print(point1.x, point1.y, point1.z)

print(Point.default_color)
print(point1.default_color)
