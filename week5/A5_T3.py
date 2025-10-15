# Course task: A5_T3 Ask name

def askName():
	return input("Insert name: ")

def greetUser(PName):
	return f"Hello {PName}!"

def main():
	print("Program starting.")
	PName = askName()
	greeting = greetUser(PName)
	print(greeting)
	print("Program ending.")
	return None

main()