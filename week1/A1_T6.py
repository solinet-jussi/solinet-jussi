# Course task: A1_T6
# Description: Create a Python program that is able to calculate remainder. Remainder can be calculated using modulo “%” operator. See also “modulus” example in W3Schools.

# Notes: Used snake_case for variable names to follow Python PEP 8 guidelines

# Prompt user "Insert an integer: " and assign the input value into feed variable
feed = input("Insert an integer: ")

# Validate input type, must be an integer
if not feed.isdigit():
    print("Error: invalid input. Please enter a valid number as an integer.")
    exit()

# Convert the feed into an integer and assign it to value variable
value = int(feed)

# Calculate the remainder of the value when divided by 2 and assign it to the remainder variable
remainder = value % 2

# Print the inserted value
print(f"Value is {value}")

# Print the remainder value
print(f"The remainder is {remainder} when {value} is divided by 2.")
