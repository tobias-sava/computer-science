# Problem Set 4
# Name: Tobias Sava
# Date: 18/03/2025
# Time Spent: 5 minutes

def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k element in Lin and
    then sorts the remaining elements in ascending order.
    Does not return anything.
    """
    # Your code here

    Lin.remove(k)

    Lin.sort()

    return None

# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]

# Solved.