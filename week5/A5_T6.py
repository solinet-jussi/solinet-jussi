
# Course task: A5_T6 Tally counter

def menu():
	print("Options:")
	print("1 - Show count")
	print("2 - Increase count")
	print("3 - Reset count")
	print("0 - Exit")
	choice = input("Your choice: ")
	return choice

def showCount(count):
	print(f"Current count - {count}")

def increaseCount(count):
	count += 1
	return count

def resetCount(count):
	count = 0
	return count

def exit():	
	print("Exiting program.")

print("Program starting.")
count = 0
while True:
	choice = menu()
	if choice == "1":
		showCount(count)
	elif choice == "2":
		count = increaseCount(count)
		print("Count increased!")
	elif choice == "3":
		count = resetCount(count)
		print("Cleared count!")
	elif choice == "0":
		exit()
		break
	else:
		print("Unknown option!")

print("Program ending.")
	