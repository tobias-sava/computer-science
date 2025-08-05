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

    try:
        for i in L: # Iterating through the list.
            if type(i) == str: # If the list type is str, adding sum to result.
                for char in i:
                    result += 1
            else: # If type is list, will access the sublist.
                for sl in i: # Accessing sublist.
                    for i in sl: # For index in sublist:
                        for char in i:
                            result += 1 # Adding 1 to result for every character.
        
        return result
    
    except:
        raise ValueError("List or sublist contains invalid object.")



# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError