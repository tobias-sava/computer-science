# 05/04/2025

def in_list(L, e):

    if len(L) == 0: # if list is empty and we do not find e, returns false
        return L[0] == e
    else:
        if L[0] == e: # when we find e, returns true
            return True
        else:
            return in_list(L[1:], e)
            # calling function recursively while creating a new list with L[0] removed