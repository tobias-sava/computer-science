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
        self.happiness += 10

    def play(self, time):
        self.happiness += time / 2
        self.energy -= time / 2
        self.hunger += time / 4

    def sleep(self, hours):
        self.energy += hours * 30
        self.hunger += hours * 15

        if hours >= 12: # if sleeping too long
            self.happiness -= hours * 10
        else:
            self.happiness += hours * 2 # increasing happiness by a bit if slept well

    def get_status(self):
        print(f"{self.name} the {self.species}")
        print(f"Hunger:    {self.hunger:.1f}")
        print(f"Happiness: {self.happiness:.1f}")
        print(f"Energy:    {self.energy:.1f}")
        print("-" * 30)

Cat_One = Pet("Alisha", "Cat")

Cat_One.sleep(9)
Cat_One.feed(100)
Cat_One.play(5)

Cat_One.get_status()