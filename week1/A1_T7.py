# Course task: A1_T7
# Description: Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km "x l per 100 km"
# Notes: Used snake_case for variable names to follow Python PEP 8 guidelines

# Print info message
print("This program calculates the car's fuel consumption.")

# Prompt user for travel distance and store in feed variable
feed = input("Enter the travel distance in kilometers: ")

# Validate input type, must be an integer
if not feed.isdigit():
    print("Error: invalid input. Please enter a valid kilometers as integers.")
    exit()

# Convert the inputfeed into an integer and assign it to distance variable
distance = int(feed)

# Prompt user for fuel type and store in feed variable
feed = input("Enter the fuel usage in liters: ")

# Validate input type, must be an integer
if not feed.isdigit():
    print("Error: invalid input. Please enter a valid fuel usage as an integer.")
    exit()

# Convert the inputfeed into an integer and assign it to fuel_usage variable
fuel_usage = int(feed)

# Calculate the consumption per 100km and round to 1 decimal place
consumption_per_100km = round(fuel_usage / distance * 100, 1)

# Print the consumption per 100km
print(f"Fuel consumption is {consumption_per_100km} l per 100km")