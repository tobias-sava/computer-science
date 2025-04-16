# 16/04/2025

class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        
        return str(self.num) + "/" + str(self.denom)

    def __float__(self):
        return self.num / self.denom
    
    def __mul__(self, oth):
        top = self.num * oth.num
        bottom = self.denom * oth.denom

        return Fraction(top, bottom)

a = Fraction(1, 4)
b = Fraction(3, 1)

c = a * b # TypeError: unsupported operand type(s) for *: 
          # 'Fraction' and 'Fraction' if dunder mul is not
          # implemented.

print(c) # prints 3/4

print(float(c)) # prints 0.75