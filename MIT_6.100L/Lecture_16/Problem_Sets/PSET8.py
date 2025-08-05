# 10/04/2025

def flatten(L):

    if len(L) == 1: # base case
        return L[0]
    else:
        return L[0] + flatten(L[1:]) # calling function recursively
    
