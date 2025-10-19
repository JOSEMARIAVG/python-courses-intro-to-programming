"""
Lesson: Functions
In this lesson, you will learn how to organize your code with functions.
A function is a block of code designed to perform a specific task.
Functions let you reuse code without duplicating it.
"""

# -----------------------------
# Intro to functions: simple example
# -----------------------------
# Define a function that adds 3 to any number
def add_three(input_var):
    output_var = input_var + 3
    return output_var

# Call the function with 10 as input
new_number = add_three(10)
print(new_number)  # Output: 13

# -----------------------------
# Naming functions
# -----------------------------
# Use lowercase letters with underscores
# Example: add_three, get_pay

# -----------------------------
# A more complex example
# -----------------------------
# Function to calculate weekly pay after 12% tax, $15/hour
def get_pay(num_hours):
    # Pre-tax pay
    pay_pretax = num_hours * 15
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - 0.12)
    return pay_aftertax

# Call the function for full-time (40 hours) and part-time (32 hours)
pay_fulltime = get_pay(40)
print(pay_fulltime)  # Output: 528.0

pay_parttime = get_pay(32)
print(pay_parttime)  # Output: 422.4

# -----------------------------
# Variable scope
# -----------------------------
# Variables inside a function (like pay_aftertax) are local
# Uncommenting the next line would raise an error:
# print(pay_aftertax)

# Variables outside functions (like pay_parttime) are global
print(pay_parttime)  # Output: 422.4

# -----------------------------
# Functions with multiple arguments
# -----------------------------
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

# Call the function with specific inputs
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, 0.22)
print(higher_pay_aftertax)  # Output: 748.8

same_pay_fulltime = get_pay_with_more_inputs(40, 15, 0.12)
print(same_pay_fulltime)    # Output: 528.0

# -----------------------------
# Functions with no arguments
# -----------------------------
def print_hello():
    print("Hello, you!")
    print("Good morning!")

# Call the function
print_hello()
# Output:
# Hello, you!
# Good morning!