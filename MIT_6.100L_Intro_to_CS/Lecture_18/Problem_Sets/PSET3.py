# 15/04/2025

class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        
        return str(self.num) + "/" + str(self.denom)

    # old multiplication method

    # def times(self, oth):
    #     top = self.num * oth.num
    #     bottom = self.denom * oth.denom
        
    #     return top / bottom

    # multiplication dunder method

    def __mul__(self, oth):
        top = self.num * oth.num
        bottom = self.denom * oth.denom

        return Fraction(top, bottom) # returns fraction obj (result)
    

    
a = Fraction(1, 4)
b = Fraction(3, 1)
print(a) # prints 1/4
print(b) # prints 3

print(type(a)) # prints <class '__main__.Fraction'>

c = a * b # this will automatically call our dunder multiplicatiom method

print(c) # printing also calls out str dunder method, so we end up getting
         # the format we implemented (fraction format).

print(a.__mul__(b)) # also a valid way of calling the method
print(Fraction.__mul__(a, b)) # also valid but full parameters must be given

# all three of the prints above return 3/4.

# as before, if str method is removed, we will only receive the memory address
# of the objects. not the result we are looking for in this case (3/4)