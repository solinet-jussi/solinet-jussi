# Course task: A2_T1: Basic program structure
# Notes: Used snake_case for variable names to follow Python PEP 8 guidelines

user_name = input("What is your name: ")
float1 = float(input("Enter a floating point number: "))
float2 = float(input("Enter second floating point number: "))

product = round(float1 * float2, 2)

print(f"{user_name}, you gave numbers {float1} and {float2}")
print(f"Multiplying first and second number will result in product {product}")