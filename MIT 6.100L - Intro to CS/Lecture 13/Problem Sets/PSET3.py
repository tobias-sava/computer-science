# 23/03/2025

# Remaking PSET2 with the use of isinstance().

# 23/03/2025

def sum_str_lengths(L):
    """
    L is a non-empty list containing either: 
    * string elements or 
    * a non-empty sublist of string elements
    Returns the sum of the length of all strings in L and 
    lengths of strings in the sublists of L. If L contains an 
    element that is not a string or a list, or L's sublists 
    contain an element that is not a string, raise a ValueError.
    """
    # Your code here  

    assert len(L) > 0, "List empty."

    result = 0

    for i in L:
        if isinstance(i, str): # If index elements are type(str).
            result += len(i) # Adding the length of str to result.
        elif isinstance(i, list): # If type(list):
            for sl in i: # Accessing sublist.
                if isinstance(sl, str): # If sl elements are type(str):
                    result += len(sl)
                else:
                    raise ValueError("Sublist contains invalid characters.") # Raising VE if sl contains non-type(str) objects.
        
        else:
            raise ValueError("List contains invalid objects.") # Raising VE if L contains invalid objects (anything besides type(str)).

    return result

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError