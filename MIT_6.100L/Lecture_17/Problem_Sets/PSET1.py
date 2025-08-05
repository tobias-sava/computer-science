# 10/04/2025

class Coordinate(object): # defining class

    def __init__(self, xval, yval): # dunder init (data that inits a Coord object)
        self.x = xval # initializing objects
        self.y = yval # can be the same variable or a different one
    
    # example:
        
    #    self.xval = xval
    #    self.yval = yval

    # both are still valid initializations

# initializing objects

origin = Coordinate(0, 0) # now a Coordinate object referred to by variable origin

c = Coordinate(3, 4) # variables (in heap) point to the
                     # object type 'Coordinate' (stack)

print(c.y) # prints 4
print(origin.x) # prints 0

print(type(c.y)) # prints <class 'int'>

