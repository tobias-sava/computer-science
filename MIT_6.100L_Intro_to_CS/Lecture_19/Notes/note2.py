# 30/04/2025

#class Parent(object):

    #class Child(object):
    
    # or

    #class Parent(object):
    
    #class Cat(Animal): <---- Passing parent class through.

    # Subclass inherits:

    # All data and behaviours of Parent
    # + Add more info
    # + Additional behaviours
    # Override behaviours

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname):
        self.name = newname
    
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
    
class Cat(Animal): # Inherits all attributes of Animal (init, set age, set name, get age, get name)
    # Uses Animal's __init__ method.

    def speak(self): # Adding new methods specific to the Cat subclass.
        print("meow")
    
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)

# All methods that work with type(Animal) will work to type(Cat)

c = Cat(5)
c.set_name("fluffy")
c.speak() # prints meow
print(c.get_age()) # prints 5

# a = Animal(1)

# a.speak() # AttributeError: 'Animal' object has no attribute 'speak'

# AttrError because the Animal class does not have the speak method.