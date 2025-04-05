# 05/04/2025

def in_lists_of_list(L, e):

    """
    L is a list whose elements are lists containing ints
    Returns True if e is an element within the lists of L
    and False otherwise.
    Hint, the in operator is useful he, i.e. e in something
    """

    print(e, L)

    if len(L) == 0: # base case
        return False
    else:
        if e in L[0]: # if e is found in the first sublist
            return True
        # else, function calls itself again, removing the first element
        # in this case, removing the first sublist
        return in_lists_of_list(L[1:], e)
        # function will keep calling itself until e is found or the list is empty and still hasn't found e.
        # if e hasnt been found and the list is empty, our base case will trigger thus returning false.


test = [[1, 2], [3, 4], [5, 6, 7]]
print(in_lists_of_list(test, 3))

# test = [[1, 2], [3, 4], [5, 6, 7]]
# print(in_lists_of_list(test, 0))
