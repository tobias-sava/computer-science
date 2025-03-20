# 19/03/2025

def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    # Your code here

    result = 0

    list = nums_list[:]

    for i in nums_list:
        for x in list:
            if i ** 2 == x:
                result += 1
    
    return result


# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3

# Solved.