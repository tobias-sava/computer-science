# 05/08/2025

# Branching 1

# Assume you're given 2 int variables: n1 and n2. 
# Print "both" if they are both positive, "only one" if only one of them is positive, and "neither" if neither are positive.

n1 = 0
n2 = 0

if n1 and n2 >= 1:
    print("both")

elif n1 or n2 >= 1:
    print("only one")

else:
    print("neither")