# 23/03/2025

def count_matches(d):
    """ d is a dict
    Returns how many entries in d have the key equal to its value """

    dlist = list(d.items()) # Creating iterable.

    result = 0 # Init result variable.

    for k, v in dlist: # Iterating through dlist for keys and values.
        if k == v:
         result += 1

    return result

# For example:
d1 = {1:2, 3:4, 5:6}
print(count_matches(d1)) # prints 0
d2 = {1:2, 'a':'a', 5:5}
print(count_matches(d2)) # prints 2