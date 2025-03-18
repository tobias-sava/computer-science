# 18/03/2025

def remove_all(L, e):
    
    while e in L:
        L.remove(e)
    
    return None


# Example of a bad use of for loop + removal:

def remove_all(L, e):

    for elem in L: # Loop iterates over the list but does not decrement
                   # by one (due to list mutating/shifting over by one), 
                   # resulting in the loop skipping a character each time.
        if elem == e:
            L.remove(e)



        