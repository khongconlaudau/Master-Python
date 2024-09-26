from Classes.Constructor import point1


class Point:
    #  __init__ is called magic method(constructor)
    # self is reference of object itself
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Also called magic method
    @classmethod
    def default(cls):
       return cls(0, 0)

    def draw(self):
        print(f"Point {self.x}, {self.y}")


point1 = Point.default()
print(point1.x, point1.y)

