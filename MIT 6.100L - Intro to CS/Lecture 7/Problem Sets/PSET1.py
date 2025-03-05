# Problem Set 1
# Name: Tobias Sava
# Date: 05/03/2025 
# Time Spent: X

# Write a code that satisfies the following specifications:

def div_by(n, d):
  '''
  n and d are ints > 0
  Returns True if d divides n evenly and False otherwise
  '''
  # Test your code with n = 10 and d = 3 / n = 195 and d = 13
  if n % d == 0:
    return True
  else:
    return False
  
  # return n % d == 0 can also be used

div_by(10, 3)
div_by(195, 13)





