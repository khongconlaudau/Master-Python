class MyPoint:
    # all functions in a class should have at least one parameter
    def draw(self):
        print("Draw")


point = MyPoint()

print(type(point))
print(isinstance(point, MyPoint))

point.draw()