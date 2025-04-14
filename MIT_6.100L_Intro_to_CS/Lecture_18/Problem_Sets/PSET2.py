# 14/04/2025

class SimpleFraction(object):
    """ A number represened as a fraction """
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def get_inverse(self):
        """ Returns a float representing 1 / self """
        return self.denom / self.num # returning inverse

    def invert(self):
        """ Set self's num to denom and vice versa.
            Returns none. """
        (self.num, self.denom) = (self.denom, self.num) # inverting with tuple

f1 = SimpleFraction(3, 4)
print(f1.get_inverse()) # returns 1.33333333
f1.invert() # returns 4, 3
print(f1.num, f1.denom)