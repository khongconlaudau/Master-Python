class Animal:
    def __init__(self):
        self.age = 1

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

        #Super() also can go at the bottom. Does not require at the top like Java


mammal = Mammal()
print(mammal.weight)
print(mammal.age)
