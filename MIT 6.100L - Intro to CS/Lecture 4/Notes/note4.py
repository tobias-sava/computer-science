# 24/02/2025

# guess and check algorithm part 2

# using a for loop instead of a while loop this time

# hardcode a number as a secret number

# write a program that checks through all the numbers from 1 to 10 and prints the secret value if its in that range

# continue from 44:18 on yt vid

secret = 9 # harcoding secret number
numfound = False # making a flag (boolean variable) to trigger not found print statement if number within range in not found

for snum in range (1, 11): # for the secret number in range 1 through 10
    if snum == secret: # if snum (1, 2, 3 etc.) is equal to our secret number:
        print(snum + 'found') # printing result
        numfound = True # number has been found
    if numfound != True: # if number is not found:
        print('number not found, get better')

# alternate way of stating if snum is not found
    if not numfound:
        print('number not found')
