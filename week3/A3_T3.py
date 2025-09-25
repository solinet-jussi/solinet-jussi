# Course task: A3_T3: Menu program

print("Program starting.")
print("This is a program with a simple menu, where you can choose which operation the program performs.")

# Prompt username first
user_name = input("Before the menu, please insert your name: ")

# Display menu options
print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")

# Prompt user to choose option
choice = input("Your choice: ")

# Perform actions based on the user input
if choice == "1":
    print(f"Welcome {user_name}!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")
