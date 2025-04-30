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

import random

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


#


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age) # calling animals init method (sets self.name = name and self.age = age)
        self.set_name(name) # setting Person object's name
        self.friends = [] # additional attribute
    
    def get_friends(self):
        return self.friends.copy()
    
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    
    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print((abs(diff)), "year difference")
    
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)
    

#


def make_pets(d):
    """ d is a dict mapping a Person obj to a Cat obj
    Prints, on each line, the name of a person,
    a colon, and the name of that persons's cat """

    d = {}

    for k, v in d.items(): 
        # k (key) person
        # v (value) cat
        print(k.get_name()) + ":" + print(v.get_name())

p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
    
    def change_major(self, major):
        self.major = major
    
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("im still zooming")

    def __str__(self):
        return "student:", + str(self.name) + ":" + str(self.age) + ":" + str(self.major)


#


class Rabbit(Animal):

    tag = 1 # variable shared across class instances

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag # rabbit obj identifier
        Rabbit.tag += 1 # keeping track of how many rabbit objs are created

    def get_rid(self):
        return str(self.rid)

r1 = Rabbit(8) # Rabbit object identifier (rid) 1
r2 = Rabbit(6) # rid 2
r3 = Rabbit(10) # rid 3

print("rid:" + r1.get_rid())