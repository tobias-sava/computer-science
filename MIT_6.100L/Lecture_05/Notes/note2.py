# 26/02/2025

if num < 0:
    is_neg == True # setting negative flag to true
    num = abs(num)
else:
    is_neg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result - str(num%2) + result
    num = num // 2
if is_neg: # recalls neg flag and executes accordingly
    result = '-' + result
