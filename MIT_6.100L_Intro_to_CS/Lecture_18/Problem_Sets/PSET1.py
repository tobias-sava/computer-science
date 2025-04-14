# 14/04/2025

class SimpleFraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
        
    def times(self, oth):
        top = self.num * oth.num # top/num
        bottom = self.denom * oth.denom # bottom/denom

        return top / bottom # returning result
    
    def plus(self, oth):
        top = self.num * oth.denom + self. denom * oth.num
        bottom = self.denom * oth.denom

        return top / bottom

f1 = SimpleFraction(3, 4)
f2 = SimpleFraction(1, 4)

print(f1.num) # prints 3
print(f1.denom) # prints 4
print(f1.plus(f2)) # prints 1.0
print(f1.times(f2)) # prints 0.1875