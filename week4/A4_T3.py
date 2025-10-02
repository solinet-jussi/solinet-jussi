# Course task: A4_T3 While-loop

print("Program starting.")

value1 = int(input("Insert starting value: "))
value2 = int(input("Insert stopping value: "))

print("\nStarting while-loop.")

i = value1

while i <= value2:
    print(f"{i}", end=" ")
    i += 1

print("\n")

print("Program ending.")
