# Problem Set 0
# Name: Tobias Sava
# Date: 02/03/2025 (refined it a little on 03/02/2025)
# Time Spent: 30 minutes

x = 54321

epsilon = 0.01

num_guesses = 0

guess = 0.0

increment = 0.0001

while abs(guess**2 - x) >= epsilon and guess ** 2 <= x:
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)

if abs(guess ** 2 - x) >= epsilon:
    print('Failed on square root of', x)
else:
    print(guess, 'is close to square root of', x)

# test cases passed successfully (questioning my existence rn)
# in conclusion: stay away from floats in order to avoid mental health deterioration
