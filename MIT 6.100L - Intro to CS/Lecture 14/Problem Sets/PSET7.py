# 23/03/2025

# Extra problems:



def sum_even_numbers(nums):
    
    result = 0

    for i in nums:
        if i % 2 == 0:
            result += i
    
    return result

# Example usage
nums = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(nums))  # Output: 12 (2 + 4 + 6)



def count_vowels(s):

    result = 0

    result_vowels = []

    vowels = ['a', 'e', 'i', 'o', 'u']

    sl = list(s.strip()) # Converting string into a stripped list.

    for i in sl:
        if i in vowels:
            result_vowels.append(i)
            result += 1
    
    return (result, result_vowels)

# Example usage
s = "Hello World"
print(count_vowels(s))  # Output: 3 (e, o, o)



def longest_word(words):

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

# Example usage
words = ["apple", "banana", "kiwi", "grape"]
print(longest_word(words))  # Output: "banana"

