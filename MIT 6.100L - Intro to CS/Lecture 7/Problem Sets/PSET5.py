# 08/03/2025

# Write a function first_unique_char(s) that takes a string s and returns the first non-repeating character. 
# If all characters repeat, return None.

def first_unique_char(s):

    result = None
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    for char in s:
        if char_count[char] == 1:
            result = char
        
            break

# Solved
