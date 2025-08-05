# 10/03/2025

# Write a function reverse_string(s) that takes a string and returns it reversed, 
# without using slicing ([::-1]).

def reverse_string(s):
    
    reversed = ""
    
    for char in s:
        reversed = char + reversed

    return reversed