# Course task: Menu-driven program

def menu():
	print("Options:")
	print("1 - Insert word")
	print("2 - Show current word")
	print("3 - Show current word in reverse")
	print("0 - Exit")
	choice = input("Your choice: ")
	return choice

def insertWord():
	word = input("Insert word: ")
	return word

def showCurrentWord(current_word):
	print(f"Current word - \"{current_word}\"")

def showCurrentWordInReverse(current_word):
	reversed_word = current_word[::-1]
	print(f"Word reversed - \"{reversed_word}\"")

def exit():
	print("Exiting program.")

print("Program starting.")
current_word = ""
while True:
	choice = menu()
	if choice == "1":
		current_word = insertWord()
	elif choice == "2":
		showCurrentWord(current_word)
	elif choice == "3":
		showCurrentWordInReverse(current_word)
	elif choice == "0":
		exit()
		break
	else:
		print("Unknown option! Try again.")
print("Program ending.")
	