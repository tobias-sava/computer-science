# 26/03/2025

def score_count(x):

    """ Return all the ways to make a score of x by adding
    1, 2 and/or 3 together. Order does not matter. """

    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    else:
        return score_count(x-1) + score_count(x-2) + score_count(x-3)
    
# score_count with dict

d = {}

def score_count_eff(x, d):

    if x in d:
        return d[x]
    elif x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    else:
        ans = score_count_eff(x-1, d) + score_count_eff(x-2, d) + score_count_eff(x-3, d)
        d[x] = ans
        return ans

print(score_count_eff(5, d))  # Example call