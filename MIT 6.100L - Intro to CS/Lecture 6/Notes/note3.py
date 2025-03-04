# 04/03/2025

# Bisection Search (Cube Root), done on my own with fixed values provided by teacher below.

cube = 27
epsilon = 0.01

low = 0
high = cube

# My code

guess = (low + high) / 2.0 # initial guess at halfway point

while abs(guess ** 3 - cube) > epsilon:
  if abs(guess ** 3) > cube:
    high = guess # updating high point to guess
  else:
    low = guess # otherwise, updating the low point
  guess = (low + high) / 2.0

print(guess, 'is within', epsilon, 'of', cube)





