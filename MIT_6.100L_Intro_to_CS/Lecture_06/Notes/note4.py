# 04/03/2025

# Newton-Raphson Root Finder

epsilon = 0.01
k = 24.0
guess = k / 2.0
num_guesses = 0

while abs(guess * guess - k) >= epsilon:
  num_guesses += 1
  guess = guess - (((guess ** 2) - k) / (2 * guess))





