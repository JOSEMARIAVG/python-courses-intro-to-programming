"""
Lesson: Data Types
In this lesson, you will learn about Python data types: integers, floats, booleans, and strings.
Data types determine what kinds of operations you can perform.
"""

# -----------------------------
# Integers
# -----------------------------
x = 14
print(x)          # Output: 14
print(type(x))    # Output: <class 'int'>

# -----------------------------
# Floats
# -----------------------------
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))  # Output: <class 'float'>

almost_pi = 22 / 7
print(almost_pi)
print(type(almost_pi))  # Output: <class 'float'>

# Round to 5 decimal places
rounded_pi = round(almost_pi, 5)
print(rounded_pi)       # Output: 3.14286
print(type(rounded_pi)) # Output: <class 'float'>

# Floats with no fractional part
y_float = 1.
print(y_float)          # Output: 1.0
print(type(y_float))    # Output: <class 'float'>

# -----------------------------
# Booleans
# -----------------------------
z_one = True
print(z_one)       # Output: True
print(type(z_one)) # Output: <class 'bool'>

z_two = False
print(z_two)       # Output: False
print(type(z_two)) # Output: <class 'bool'>

z_three = (1 < 2)
print(z_three)       # Output: True
print(type(z_three)) # Output: <class 'bool'>

z_four = (5 < 3)
print(z_four)       # Output: False
print(type(z_four)) # Output: <class 'bool'>

# Using not to switch boolean values
z_five = not z_four
print(z_five)       # Output: True
print(type(z_five)) # Output: <class 'bool'>

# -----------------------------
# Strings
# -----------------------------
w = "Hello, Python!"
print(w)          # Output: Hello, Python!
print(type(w))    # Output: <class 'str'>
print(len(w))     # Output: 14

# Empty string
shortest_string = ""
print(type(shortest_string))  # Output: <class 'str'>
print(len(shortest_string))   # Output: 0

# Strings containing numbers
my_number = "1.12321"
print(my_number)   # Output: 1.12321
print(type(my_number))  # Output: <class 'str'>

# Convert string to float
also_my_number = float(my_number)
print(also_my_number)   # Output: 1.12321
print(type(also_my_number))  # Output: <class 'float'>

# Concatenate strings
new_string = "abc" + "def"
print(new_string)    # Output: abcdef
print(type(new_string)) # Output: <class 'str'>

# Multiply string by integer
newest_string = "abc" * 3
print(newest_string)     # Output: abcabcabc
print(type(newest_string)) # Output: <class 'str'>

# Attempting to multiply string by float will raise an error
# Uncomment the next line to see the error:
# will_not_work = "abc" * 3.0
# TypeError: can't multiply sequence by non-int of type 'float'