# 10/03/2025

# Write a function count_evens(lst) that takes a list of 
# integers and returns the number of even numbers in the list.

def count_evens(lst):

    evens = 0

    for n in lst:
        if n % 2 == 0:
            evens += 1
    
    return evens