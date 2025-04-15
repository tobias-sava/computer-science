# 15/04/2025

class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.denom)

a = Fraction(1, 4)
b = Fraction(3, 1)
print(a) # prints 1/4
print(b) # prints 3