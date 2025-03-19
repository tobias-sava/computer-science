# 18/03/2025

# 1. Basic Nested Function
# Write a function outer_function that defines an inner 
# function inner_function. The inner function should 
# return a greeting message, and the outer function 
# should call it and return its result.

def outer_function():
    def inner_function():
        return "Greetings."
    
    return inner_function()

# Solved.

# 2. Calculator with Nested Functions
# Write a function calculator(operation, a, b) that 
# contains nested functions for addition, subtraction, 
# multiplication, and division. Based on the operation 
# argument ("add", "subtract", "multiply", "divide"), 
# the correct inner function should be called and return 
# the result.

def calculator(operation, a, b):
    
    def add():
        return a + b
    
    def subtract():
        return a - b
    
    def multiply():
        return a * b
    
    def divide():
        return a / b
    
    if operation == "add":
        return add()
    elif operation == "subtract":
        return subtract()
    elif operation == "multiply":
        return multiply()
    else:
        return divide()

print(calculator("add", 5, 3))        # Should return 8
print(calculator("subtract", 10, 4))  # Should return 6
print(calculator("multiply", 6, 2))   # Should return 12
print(calculator("divide", 8, 2))     # Should return 4.0

# Solved.

# 3. Power Function with Nested Scope
# Write a function power(base, exponent) that defines an inner function 
# calculate() to compute base raised to the power of exponent. 
# The outer function should return the result of calling calculate().

def power(base, exponent):
    
    def calculate():
        return base ** exponent
    
    return calculate()

print(power(2, 3))  # Should return 8 (2^3)
print(power(5, 2))  # Should return 25 (5^2)
print(power(10, 0)) # Should return 1 (any number to the power of 0 is 1)

# 4. String Manipulation with Nested Functions
# Write a function process_string(string) that contains two nested functions:

# to_uppercase(): Converts the string to uppercase.
# reverse_string(): Reverses the string.
# The outer function should:

# First call to_uppercase() to convert the string to uppercase.
# Then call reverse_string() to reverse the uppercase string.
# Finally, return the result of the reversed uppercase string.

def process_string(string):
    
    def to_uppercase():
        return string.upper()
    
    uppercased_string = to_uppercase()

    result = uppercased_string[::-1]

    return result

print(process_string("hello"))  # Should return "OLLEH"
print(process_string("world"))  # Should return "DLROW"

# Solved.

# 5. Nested Function for Even/Odd Check
# Write a function check_number(number) that:

# Contains an inner function is_even() to check if the number is even.
# Contains an inner function is_odd() to check if the number is odd.
# The outer function should return a string:
# "Even" if the number is even.
# "Odd" if the number is odd.

def check_number(number):

    def is_even():
        return number % 2 == 0
    
    def is_odd():
        return number % 2 != 0
    
    if is_even():
        return "Even"
    else:
        return "Odd"
    
print(check_number(4))  # Should return "Even"
print(check_number(7))  # Should return "Odd"

# Solved.