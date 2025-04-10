# 02/03/2025

# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string
# containing the even indexed characters of my_str.

# For example, if my_str = "abcdefg" then your code should print out aceg.

my_str = "abcdefg" # storing string
counter = 0 # keeping track of evens, starting with a fixed value of 0
result = "" # storing result

while counter < len(my_str): # creating while loop (while counter is less than the strings length)
    result += my_str[counter] # adding our even indexed characters to the final result
    counter += 2 # incrementing by 2 since we only want evens

print(result)

# code execution was successful, all test cases passed
