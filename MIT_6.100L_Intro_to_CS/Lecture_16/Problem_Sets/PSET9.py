# 10/04/2025

def my_rev(L):

    if len(L) == 1: # base case
        return L
    else:
        return my_rev(L[1:]) + [L[0]] # calling function