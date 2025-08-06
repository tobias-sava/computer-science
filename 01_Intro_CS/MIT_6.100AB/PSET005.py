# 06/08/2025

# Loops 2
# Set a variable named myrange to have the value some range. 
# Set up a positive number in a variable called num. * For example:

"""
myrange = range(1,7)
num = 2
"""

# Print the last number in myrange that is divisible by num and break out of the loop immediately.

myrange = range(2, 21)
num = 4

results_list = []

for n in myrange:
    if n % num == 0:
        results_list.append(n)

print(results_list[-1])