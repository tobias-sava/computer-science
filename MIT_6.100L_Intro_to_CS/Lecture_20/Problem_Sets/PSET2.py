# 08/05/2025

class Animal:

    def __init__(self, name, species, age, adopted=False):
        self.name = name
        self.species = species
        self.age = age
        self.adopted = adopted

    def __str__(self):
        return f"{self.name} is a {self.species} aged {self.age}. Adoption status is {self.adopted}."
    
class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def bark(self):
        return f"{self.name}: WOOF!"
    
    def __str__(self):
        super().__str__
        self.bark()

class Cat(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, "Cat", age)
        self.breed = breed
    
    def meow(self):
        return f"{self.name}: MEOW!"