# 04/03/2025

# Bisection Search (Square Root), presented by teacher.

x = 54321
epsilon = 0.01
num_guesses = 0

low = 0
high = x
guess = (high + low) / 2.0

while abs(guess ** 2 - x) >= epsilon:
  if guess ** 2 < x:
    low = guess
  else:
    high = guess
  guess = (high + low) / 2.0
  num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
