"""
Welcome to the Intro to Programming course!
This course is for beginners who have never written a line of code.
You will learn Python basics to prepare for data science and machine learning.
"""

# -----------------------------
# Printing
# -----------------------------
# One of the simplest tasks is to print a message.
print("Hello, world!")  # Output: Hello, world!

# -----------------------------
# Arithmetic
# -----------------------------
# You can print the result of calculations
print(1 + 2)  # Addition -> 3
print(9 - 5)  # Subtraction -> 4
print(2 * 4)  # Multiplication -> 8
print(6 / 3)  # Division -> 2.0
print(3 ** 2) # Exponent -> 9

# Control order of operations with parentheses
print(((1 + 3) * (9 - 2) / 2) ** 2)  # Output: 196.0

# -----------------------------
# Comments
# -----------------------------
# Comments help explain your code
# Python ignores lines starting with #
# Example:
# Multiply 3 by 2
print(3 * 2)  # Output: 6

# -----------------------------
# Variables
# -----------------------------
# Create a variable and assign a value
test_var = 4 + 5
print(test_var)  # Output: 9

# Change the value of a variable
my_var = 3
print(my_var)  # Output: 3
my_var = 100
print(my_var)  # Output: 100

# Using multiple variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)  # Output: 126144000

# Adjust for leap years
days_per_year = 365.25
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)  # Output: 126230400.0

# -----------------------------
# Debugging
# -----------------------------
# A common error is a typo in variable names
# Uncomment the next line to see an error
# print(hours_per_dy)  # NameError: name 'hours_per_dy' is not defined

# Correct variable
print(hours_per_day)  # Output: 24
