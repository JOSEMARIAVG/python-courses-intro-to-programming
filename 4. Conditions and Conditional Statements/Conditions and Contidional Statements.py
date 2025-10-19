"""
Lesson: Conditions and Conditional Statements
In this lesson, you'll learn how to use conditions and conditional statements
to modify how your functions run.
"""

# -----------------------------
# Simple conditional example
# -----------------------------
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update message only if temperature is greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))  # Output: Normal temperature.
print(evaluate_temp(39))  # Output: Fever!

# -----------------------------
# if ... else statement
# -----------------------------
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37))  # Output: Normal temperature.

# -----------------------------
# if ... elif ... else statement
# -----------------------------
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

print(evaluate_temp_with_elif(36))  # Output: Normal temperature.
print(evaluate_temp_with_elif(34))  # Output: Low temperature.

# -----------------------------
# Conditional statements in calculations
# -----------------------------
def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = 0.25 * earnings
    else:
        tax_owed = 0.30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)  # Output: 2250.0
print(bob_taxes)  # Output: 4500.0

# -----------------------------
# Function with multiple elif statements
# -----------------------------
def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

print(get_dose(12))  # Output: 5