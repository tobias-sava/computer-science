# 06/08/2025

# Branching 3 [QUIZ-LEVEL] 

# Assume you're given 2 int variables: n1 and n2. 
# If both are positive, print the sum of the first digits in each. 
# If both are negative, print the sum of the last digits in each. 
# If only one is positive and the other is not, print the result when you divide the last digit by the first digit of the positive n.

n1_input = input("Enter N1: ")
n2_input = input("Enter N2: ")
result = 0

n1 = int(n1_input)
n2 = int(n2_input)

if n1 > 0 and n2 > 0:
    n1_first_digit = n1_input.lstrip('-')[0]
    n2_first_digit = n2_input.lstrip('-')[0]

    result = int(n1_first_digit) + int(n2_first_digit)
    print(result)

elif n1 < 0 and n2 < 0:
    n1_last_digit = n1_input[-1]
    n2_last_digit = n2_input[-1]

    result = int(n1_last_digit) + int(n2_last_digit)
    print(result)

else:
    if n1 > 0:
        n1_first_digit = n1_input[0]
        n1_last_digit = n1_input[-1]
        result = int(n1_last_digit) / int(n1_first_digit)
        print(result)
    else:
        n2_first_digit = n2_input[0]
        n2_last_digit = n2_input[-1]
        result = int(n2_last_digit) / int(n2_first_digit)
        print(result)