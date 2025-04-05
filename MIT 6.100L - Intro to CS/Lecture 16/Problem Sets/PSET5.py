# 05/04/2025

def total_len_recur(L):

    if len(L) == 1: # base case
        return len(L[0]) # returning the only element in L
    else:
        return total_len_recur(L[1:]) + len(L[0]) 
        # calling function recursively and removing first element while also adding its length
test = ["ab", 'c', "defgh"]
print(total_len_recur(test))

def in_list(L, e):
    
    print(L, e)

    if len(L) == 1:
        return L[0] == e # if L[0] == element we are looking for, returns true/false
    else:
        if L[0] == e:
            return True
        else:
            return in_list(L[1:], e)

test = [2,1,8,8]
print(in_list(test, 1))