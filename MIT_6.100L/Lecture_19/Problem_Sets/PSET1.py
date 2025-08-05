# 29/04/2025

class Animal:
    pass

def animal_dict(L):
    """
    L is a list
    
    Returns a dict, d, mapping an int to an Animal object.
    A key in d is all non-negative ints, n, in L. 
    A value corresponding to a key is an Animal object with n as its age. """

    d = {} # init empty dict

    for n in L:
        if type(n) == int and n >= 0: # checking if positive int
            d[n] = Animal(n)

    return d

# Returns memory address of a dict value {n: Animal(n)}

L = [1, 3, 4]
animals = animal_dict(L)
for n, a in animals.items():
    print(f"key {n} with val {a}")

# Now returns the list in a readable format.