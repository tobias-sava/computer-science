# 26/03/2025

# You have n stairs, and you can climb either 1 or 2 steps at a time. 
# How many distinct ways can you reach the top (the nth stair)?

d = {}

def stairs(n, d):

    if n in d: # if n in dict
        return d[n]
    elif n == 0: # base case
        return 1
    elif n == 1: # base case
        return 1
    else: # recursive formula
        ans = stairs(n-1, d) + stairs(n-2, d)
        d[n] = ans
        return ans
    
print(stairs(5, d))  # prints 8