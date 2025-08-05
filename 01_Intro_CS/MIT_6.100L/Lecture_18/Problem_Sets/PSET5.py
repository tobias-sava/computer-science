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

    def reduce(self):
        def gcd(n, d): # greatest common divisor 
                       # (function, NOT a method since no self)
            while d != 0:
                (d, n) = (n % d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1:
            return Fraction(self.num, 1) # must create fraction obj otherwise 
                                         # operations will be unsupported.
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num / greatest_common_divisor)
            bottom = int(self.denom / greatest_common_divisor)

        return Fraction(top, bottom)


a = Fraction(4, 1)
b = Fraction(3, 9)

ar = a.reduce()
br = b.reduce()

print(ar, type(ar))
print(br, type(br))

c = ar * br