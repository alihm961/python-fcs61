class Animal:  # Parent class
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        return "Some generic animal sound"
    
class Bird(Animal):
    def make_sound(self):
        return "Chirp Chirp"

class Fish(Animal):
    def make_sound(self):
        return "Blub Blub"
    
class Mammal(Animal):
    def make_sound(self):
        return "Bark"
    
def animal_sound(animal):
    print(f"{animal.name} makes sound: {animal.make_sound()}")
    
sparrow = Bird("Sparrow")
shark = Fish("Shark")
lion = Mammal("Lion")

animal_sound(sparrow)
animal_sound(shark)
animal_sound(lion)
