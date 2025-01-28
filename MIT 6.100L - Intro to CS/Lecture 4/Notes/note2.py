# 28/01/2025

# loop practice lol

mysum = 0 # keeping track of loops
for i in range (5, 11, 2):
  mysum += i # adding i to loop count
  if mysum == 5:
    break
    mysum += 1

# should check how many even numbers there are in range(x)

mysum = 0
for i in range (10):
  mysum += 1 
  even_nums = 0 # keeping track of evens
  if i % 2 == 0:
    even_nums += 1 # adding 1 for every even number

# going to try storing the even numbers as they are

even_nums = []
mysum = 0 
for i in range(10):
  mysum += 1
  # even_nums = [] - mistake, placed list variable outside of for loop
  if i % 2 == 0:
    even_nums.append(i)

# counting number of letters in a string exercise

s = 'abca' # string
seen = '' # seen letters
count = 0 # keeping count of loop

for char in s: 
  if char not in seen: # if char is not in seen
    seen = seen + char
    count += 1  
  else:
    pass









