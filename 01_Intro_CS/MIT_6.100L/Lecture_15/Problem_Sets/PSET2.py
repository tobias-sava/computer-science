# 25/03/2025

def recur_fact(n):

    if n == 0 or n == 1:
        return 1
    
    else:
        return n * recur_fact(n - 1)
    
print(recur_fact(5))  # Should return 120 (5 * 4 * 3 * 2 * 1)
print(recur_fact(0))  # Should return 1 (special case, 0! = 1)

def sum_of_n(n):

    if n == 0:
        return 0
    
    else:
        return n + sum_of_n(n - 1)
    
print(sum_of_n(5))  # Should return 15 (5 + 4 + 3 + 2 + 1)
print(sum_of_n(0))  # Should return 0 (special case)

def fibonacci(n):

    if n == 0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(5))  # Should return 5 (F(5) = 5)
print(fibonacci(0))  # Should return 0 (F(0) = 0)
print(fibonacci(1))  # Should return 1 (F(1) = 1)
print(fibonacci(7))  # Should return 13 (F(7) = 13)

# All 3 solved.