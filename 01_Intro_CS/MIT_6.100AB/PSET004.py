# 06/08/2025

# Loops 1 

# Set a variable named myrange to have the value some range. 
# Set up a positive number in a variable called num. * For example:

"""
myrange = range(1,7)
num = 2
"""

# Print the first number in myrange that is divisible by num and break out of the loop immediately.

myrange = range(1, 21)
num = 3

for n in myrange:
    if n % num == 0:
        print(n)
        break