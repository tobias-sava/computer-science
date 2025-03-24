# 23/03/2025

def power_recur(n, p):

    if p == 0:
        return 1
    
    elif p == 1:
        return n
    
    else:
        return n * power_recur(n, p - 1)
    
print(power_recur(3, 4)) # Prints 81

# Solved.