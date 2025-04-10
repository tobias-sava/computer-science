# 10/04/2025

class Pet:
    def __init__(self, name, species, hunger=50, happiness=50, energy=50):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def feed(self, amount):
        
        self.hunger = max(self.hunger - amount, 0)

        self.hunger -= amount
        self.happiness += 10

    def play(self, time):
        pass
