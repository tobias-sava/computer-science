# 26/02/2025

# x == float
# p == multiplicable power of 2 than makes X an int

counter = 0

x = 0.375
p = 0

# formula for finding P
while ((2 ** p) * x) % 1) != 0:
    print('Remainder = ' + str((2 ** p) * x - int((2 ** p) * x)))

num = int(x * (2 ** p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2)
    counter += 1
