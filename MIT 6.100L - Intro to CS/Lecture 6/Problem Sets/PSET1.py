# 04/03/2025


# Assume you are given an integer 0 \<= N \\<= 1000. 
# Write a piece of Python code that uses bisection search to guess N. 
# The code prints two lines: count: with how many guesses it took to find N, 
# and answer: with the value of N. 
# * Hint: If the halfway value is exactly in between two integers, choose the smaller one.

# 

# Problem Breakdown

# We are given an int in range 0 - 1000 included.
# Using bisection search, find N.
# Once found, print count and answer.

n = 552
count = 0 

low = 0
high = 1000

answer = (low + high) // 2 # * In relation to hint - using int division so it automatically rounds down for me

while answer != n: 
  if answer > n:
    high = answer - 1 # setting new high point, subtracting 1 to avoid potential infinite looping
    count += 1
    answer = (low + high) // 2
  else:
    low = answer + 1 
    count += 1
    answer = (low + high) // 2

print(f'It took {count} guesses to find N')
print(f'The value of N is {n}')

# Solved!