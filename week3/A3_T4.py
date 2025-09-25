# Course task: A3_T4: More menu options

print("Program starting.")
print("This is a program with a simple menu, where you can choose which operation the program performs.")

# Prompt username first
user_name = input("Before the menu, please insert your name: ")

# Display menu options
print("\nOptions:")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

# Prompt user to choose option
choice = input("Your choice: ")

# Perform actions based on the user input
if choice == "1":
    print(f"Welcome {user_name}!")
elif choice == "2":
    print(f"Your name backwards is {user_name[::-1]}")
elif choice == "3":
    print(f"The first character of your name is {user_name[0]}")
elif choice == "4":
    print(f"There are {len(user_name)} characters in the name {user_name}")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")
