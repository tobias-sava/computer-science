# 07/08/2025

# Loops 3 

# Rewrite the loop so the loop variable is over the string itself

"""
s = "strings are cool"
for i in range(len(s)):
    if s[i] != ' ':
        print(s[i])
"""

s = "strings are cool"

for char in s:
    if char != " ":
        print(char)