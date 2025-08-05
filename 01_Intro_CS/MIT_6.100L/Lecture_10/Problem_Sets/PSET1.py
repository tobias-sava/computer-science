# 17/03/2025

def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here

    for func in Lf: # Iterates through the list of functions.
        if not func(n): # If any function return False, all_true returns False immediately.
            return False
    return True # If all functions return True, all_true returns True.

# Example functions:

def is_positive(x):
    return x > 0

def is_even(x):
    return x % 2 == 0

# Example usage:
print(all_true(6, [is_positive, is_even]))  # This should return True
print(all_true(5, [is_positive, is_even]))  # This should return False

# Solved