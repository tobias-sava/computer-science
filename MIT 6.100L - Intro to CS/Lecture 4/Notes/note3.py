# 28/01/2025

# guess and check algorithm

# applies to problems where:
# - you are able to guess a value for a solution
# - you are able to check if the solution is correct

# you can keep guessing until:
# - solution found
# - all values/guesses have been exhausted (not able to find a solution)

# finding the root of a perfect square

# given an int x; we want to see if there is another int which is its square root.

# if guess squared is bigger than x, we can stop

guess = 0 # guess count
neg_flag = False # neg flag false by default

x = int(input("Enter an integer: ")) # taking int input from user

if x < 0:
  neg_flag = True # flagging negative numbers

while guess ** 2 < x: # while sq root of guess is less than x:
  guess += 1 # keeping count
if guess ** 2 == x:
  print(f"Square root of {x} is {guess}.")
else:
  print(f"{x} is not a perfect square.")
  if neg_flag:
    print(f"Just checking ... did you mean {-x}?")

# Enter an integer: -5
# -5 is not a perfect square.
# Just checking ... did you mean 5?