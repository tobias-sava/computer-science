# 26/02/2025

# Converting a float into binary

num =
result = ''

if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2

print(result)
