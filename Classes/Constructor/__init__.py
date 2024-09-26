class Point:
    #  __init__ is called magic method(constructor)
    # self is reference of object itself
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point {self.x}, {self.y}")

point1 = Point(y=2, x=1)
point1.draw()

