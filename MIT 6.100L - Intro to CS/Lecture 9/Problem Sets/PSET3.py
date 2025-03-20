# 15/03/2025

# 1. Sum of Elements in a Tuple

# Given a tuple of numbers, write a lambda function to find the sum of all elements.

nums = (1, 2, 3, 4)

sum_of_elements = lambda nums : sum(nums)

# 2. Sorting Tuples by Second Element

# You have a list of tuples, where each tuple contains a name and an age. 
# Use a lambda function to sort the list based on the age (second element of the tuple).

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

sorted_people = sorted(people, key = lambda person : person[1]) # Sorting by age.

print(sorted_people)

# 3. Filtering Even Numbers in a Tuple
# Write a lambda function that filters out even numbers from a tuple and 
# returns a new tuple with only odd numbers.

nums = (1, 2, 3, 4, 5, 6)

filter_odd = lambda nums : tuple(filter(lambda x : x % 2 != 0, nums))

result = filter_odd(nums)

print(result)

# 4. Find the Maximum Tuple
# Given a list of tuples, each containing two integers, use a lambda function to 
# find the tuple with the highest sum of its elements.

tuples = [(1, 2), (3, 4), (5, 6)]

highest_sum = max(tuples, key = lambda x : x[0] + x[1]) # Adds each tuple pair then uses max function to find the highest one.

# 5. Create a Tuple of Squares
# Given a tuple of numbers, use a lambda function to create a new tuple where each element is the square of the original element.

nums = (1, 2, 3, 4)

squared_tuple = tuple(map(lambda x : x ** 2, nums))

print(squared_tuple)

# All solved.
