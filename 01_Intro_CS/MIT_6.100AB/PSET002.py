# 05/08/2025

# Branching 2 Assume you're given 2 int variables: n1 and n2. 
# Print "both" if they both have a 0 as one of their digits, "only one" if only one of them has a 0, and "neither" if neither has a 0.

n1 = 1
n2 = 1

def has_zero(n1, n2):

    n1 = str(n1)
    n2 = str(n2)

    n1status = None
    n2status = None

    for n in n1:
        if n == "0":
            n1status = True
        else:
            n1status = False

    for n in n2:
        if n == "0":
            n2status = True
        else:
            n2status = False

    if n1status and n2status == True:
        print("both")
    
    elif n1status or n2status == True:
        print("only one")
    
    else:
        print("neither")

has_zero(n1, n2)