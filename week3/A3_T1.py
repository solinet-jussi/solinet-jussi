# Course task: A3_T1: If-statements

print("Program starting.")
print("Insert two integers.")

num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))

print("Comparing inserted integers.")

# Integer comparison
# Case 1: integers are equal
if num1 == num2:
    print("Integers are the same")
# Case 2: First integer is greater than second integer
elif num1 > num2:
    print("First integer is greater than second integer")

# Sum of the integers
print("\nAdding integers together")
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")

# Checking the parity of the sum with modulo operator	
print("\nChecking the parity of the sum")
if sum % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")

print("Program ending.")
