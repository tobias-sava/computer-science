# Problem Set 0
# Name: Tobias Sava
# Date: 23/01/2025
# Time Spent: 30 seconds

# Simple class exercise:

# 1. Ask user for a verb.
# 2. Print "I can _ better than you" where you replace _ with the verb.
# 3. Then prints the verb 5 times in a row separated by spaces.

user_verb = input("Type a verb: ")

print("I can " + user_verb + " better than you!")

print((user_verb + " ") * 4 + " " + user_verb) # Multiplied by 4 in order to prevent last character being occupied by a space.

# Resolved and checked with tutor. Correct!