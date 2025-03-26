# 26/03/2025

# Recursive Fibonacci function utlizing dict for efficiency.

def fib_efficient(n, d): # n number, d dict

    if n in d: # checking n has already been calculated
        return d[n] # if calculated, return n
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans # adding new entry
        return ans
    
d = {1:1, 2:1}
print(fib_efficient(6, d)) # prints 8

# Solved.

# Calling fib(34) results in 11.4 million function calls.

# Calling fib(34) with the use of dict to store already
# already solved answers uses 65 function calls.