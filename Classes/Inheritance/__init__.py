    # **** We should avoid multi inheritance (ideal is 1 - 2 level)

class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print('eating')

class Mammal(Animal):
    def walk(self):
        print('walking')

class Fish(Animal):
    def swim(self):
        print('swimming')


animal = Mammal()
print(animal.age)
animal.eat()