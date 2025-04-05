# 05/04/2025

def print_list(lst):

    if len(lst) == 0: # base case
        return
    print(lst[0]) # processing the first element
    print_list(lst[1:]) # recursively calling the function

my_list = ["apple", "banana", "cherry"]
print_list(my_list)