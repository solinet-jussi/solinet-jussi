# Course task: A3_T5: Temperature converter

print("Program starting.")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = input("Your choice: ")

if choice == "1":
    celsius = float(input("Enter the amount in Celsius: "))
    fahrenheit = round((celsius * 1.8) + 32, 1)
    print(f"{celsius} °C equals to {fahrenheit} °F")
elif choice == "2":
    fahrenheit = float(input("Enter the amount in Fahrenheit: "))
    celsius = round((fahrenheit - 32) / 1.8, 1)
    print(f"{fahrenheit} °F equals to {celsius} °C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")