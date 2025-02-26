# Problem Set 0
# Name: Tobias Sava
# Date: 24/02/2025
# Time Spent: 5 minutes

# Assume you are given a positive integer variable named N.
# Write a piece of Python code that finds the cube root of N.
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube.

cube = int(input("Enter a positive integer: ")) # collecting int from user and storing in variable

for guess in range(abs(cube)+1): # loops through the absolute cube + 1 (+1 is added to skip 0 cube error)
    if guess ** 3 >= abs(cube): # if the guess cubed is bigger or equal to abs(user input)
        break # breaking here
if guess ** 3 != abs(cube): # if guess cubed does not equal user input
    print(cube, "is not a perfect cube") # prints result (non cube)
else:
    if cube < 0: # if cube is negative
        guess = -guess # since positive/negative roots are the same, im handling negative number scenarios by simply making the guess negative
    print("Cube root of" + str(cube) + " is " + str(guess)) # prints result (cube)

# test case passed successfully
