# 23/03/2025

def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a 
    positive value.
    """
    # Your code here  

    positive_keys = [] # Init empty list.

    for k, v in d.items():
        if sum(v) > 0:
            positive_keys.append(k) # Appending the key of positive list sum to positive_keys list.
    
    positive_keys.sort() # Sorting the keys.

    return positive_keys # Returning final result (sorted keys).


# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]