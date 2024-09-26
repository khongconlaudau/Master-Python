class Dog:
    def say(self):
        print("Guw guw")

class Cat:
    def say(self):
        print("meow meow")

def say(animals):
    for animal in animals:
        animal.say()

dog = Dog()
cat = Cat()
say([cat, dog])
