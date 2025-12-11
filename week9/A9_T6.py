########################################################
# Task A9_T6
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

def showOptions() -> None:
	# TODO: Print the menu options
	print("Options:")
	print("1 - Insert line")
	print("2 - Save lines")
	print("0 - Exit")

def askChoice() -> int:
	# TODO: Ask user for a menu choice and return it as an integer
	# Students should use try-except to handle invalid input
	try:
		choice_str = input("Your choice: ")
		return int(choice_str)
	except ValueError:
		return -1

def saveLines(PLines: list[str]) -> None:
	# TODO: Ask for filename and save lines to the file
	# Students should use try-except to handle file errors
	try:
		filename = input("Insert filename: ")
		with open(filename, 'w', encoding='UTF-8') as f:
			f.writelines(PLines)
	except Exception:
		# Handle file errors silently or with appropriate error handling
		pass

def insertLine(PLines: list[str]) -> None:
	# TODO: Ask user to input a line and add it to PLines
	text = input("Insert text: ")
	PLines.append(text + '\n')

def onInterrupt(PLines: list[str]) -> None:
	# TODO: Handle KeyboardInterrupt when there are unsaved lines
	# Students should use try-except to handle input errors
	if len(PLines) == 0:
		print("Closing suddenly.")
	else:
		print("Keyboard interrupt and unsaved progress!")
		try:
			response = input("Save before quit(y/n)?: ")
			if response.lower() == 'y':
				saveLines(PLines)
		except Exception:
			# Handle any input errors during interrupt handling
			pass

def main() -> None:
	Lines: list[str] = []
	Choice = -1
	print("Program starting.")
	# Wrap the main loop in a try-except block to catch KeyboardInterrupt
	try:
		while Choice != 0:
			showOptions()
			Choice = askChoice()
			if Choice == 1:
				insertLine(Lines)
			elif Choice == 2:
				saveLines(Lines)
			elif Choice == 0:
				print("Exiting program.")
			else:
				print("Unknown option!")
			print("")
	except KeyboardInterrupt:
		onInterrupt(Lines)
	Lines.clear()
	print("Program ending.")

if __name__ == "__main__":
	main()
