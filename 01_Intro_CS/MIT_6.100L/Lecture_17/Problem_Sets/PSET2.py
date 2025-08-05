# 10/04/2025

class Coordinate(object):

    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    
    def distance(self, other): # simple pythagoras' theorem application
        x_diff_sq = (self.x-other.x) ** 2
        y_diff_sq = (self.y-other.x) ** 2
        
        return (x_diff_sq + y_diff_sq) ** 0.5
    
# dot notation

# the "." operator is used to access any attribute:

    # a data attribute of an object (for example c.x)
    # a method of an object

# usage example:

# <object_variable>.<method>(parameters)

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

# usage example:

print(c.distance(origin)) # will calc the distance from c -> orig
                          # based on our distance function

# conventional way above, equivalent version below:

c = Coordinate(3, 4)
origin = Coordinate(0, 0)

print(Coordinate.distance(c, 0)) 
    