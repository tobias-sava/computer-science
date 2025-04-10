# 25/01/2025

# Assume you are given a positive integer variable named N. 
# Write a piece of Python code that prints hello world on separate lines, N times. 
# You can use either a while loop or a for loop.

n = 10

count = 0 # keeping count of loops

while count < n: # while the count is lower than N:
  count += 1 # adding to count
  print("hello world")

# Resolved and self-checked, correct.


# ---------------------------------------------------------


# quick factorial exercise

x = 4

i = 1

factorial = 1 # running product

while i <= x:
  factorial *= i # multiplying by loop variable each time
  i += 1

print(f"{x} factorial is {factorial}")

# Self-checked, correct.