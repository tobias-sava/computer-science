# 18/03/2025

# List Comprehensions

# Create a new list by applying a function to every element
# of another iterable that satisfies a test.

# [ expression for element in List if condition]

L = ["dummy", "list"]

def f(L):
    
    Lnew = []

    for e in L:
        Lnew.append(e ** 2)
    
    return Lnew

# Can be written as a comprehension:

Lnew = [e ** 2 for e in L]

# Another example:

def f(L):
    
    Lnew = []

    for e in L:
        if e % 2 == 0:
            Lnew.append(e ** 2)
    
    return Lnew

# Can be written as a comprehension:

Lnew = [e ** 2 for e in L if e % 2 == 0]

# We use list comprehensions simply for readability/simplicity.

# List comprehensions may be marginally faster than a usual function.
