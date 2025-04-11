# 12/04/2025

class Car:
    def __init__(self, make, model, year, fuel=0):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel

    def drive(self, distance):
        if self.fuel > distance / 10:
            self.fuel -= distance / 10
        else:
            print("Not enough fuel.")

    def refuel(self, amount):
        self.fuel += amount

        if self.fuel >= 100:
            self.fuel = 100
            print("Fuel tank full.")

    def get_fuel_level(self):
        return self.fuel
    
    def age(self, current_year):
        return current_year - self.year

