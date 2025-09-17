# Course task: A1_T5 Calculate area
# Description: Make a Python program which can take user inputs and convert them into integers.
# Bonus task: test the program with different inputs e.g. decimals and correct the potential issues.

# Notes: Created input validation to check if the input is an integer. Used snake_case for variable names to follow PEP 8 guidelines

print("Calculate the area of a wall.")

# Prompt user for width and store in feed variable
feed = input("Enter the width in meters: ")
# Validate width input
if not feed.isdigit():
    print("Error: invalid input for width. Please enter a valid number as an integer.")
    exit()
# Convert the feed variable into an integer and store it in width variable
width = int(feed)

# Prompt user for height and store in feed variable
feed = input("Enter the height in meters: ")
# Validate height input
if not feed.isdigit():
    print("Error: invalid input for height. Please enter a valid number as an integer.")
    exit()
# Convert the feed variable into an integer and store it in height variable
height = int(feed)

print(f"Width is {width} m and height is {height} m.")

# Multiply width and height, then store the result in area variable
area = width * height

print(f"The wall will be {area} square meters.")
