# 18/03/2025

def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None
    """

    temp_list = []

    for i in L: # Looping through L's indexes.
        if i != e: # If each value is not equal to the value we want to remove:
            temp_list.append(i) # We append that value to our temporary list.
    
    L.clear() # Clearing the original list since we have stored the values we want.

    for e in temp_list: # Iterating through our temporary list and appending the value(s) to the original list.
        L.append(e)

    return None # We can return none since we did not create a new object - we mutated the existing L (list).

L = [1, 2, 2, 2]

remove_all(L, 2)

print(L)

# Solved.