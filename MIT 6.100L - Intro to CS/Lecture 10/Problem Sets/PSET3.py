# 17/03/2025

def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elemnts equal to e.
    """

    new_list = []

    for elem in L:
        if elem != e:
            new_list.append(elem)
    
    return new_list

L = [1, 2, 2, 2]
print(remove_elem(L, 2))