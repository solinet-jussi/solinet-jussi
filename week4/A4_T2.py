# Course task: A4_T2 For-loop 2

print("Program starting.")

value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))

print("\nStarting for-loop.")

for i in range(value1, value2 + 1):

    if i < value2:
        print(f"{i}", end=" ")

    if i == value2:
        print(f"{i}", end="\n\n")

print("Program ending.")
