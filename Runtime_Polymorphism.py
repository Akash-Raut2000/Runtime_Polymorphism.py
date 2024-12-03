class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Runtime polymorphism
animals = [Animal(), Dog(), Cat()]
for animal in animals:
    print(animal.sound())
