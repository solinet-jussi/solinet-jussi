########################################################
# Task A10_T7
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################
import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
	"""
	The "PMineField" is pre-initialized 2d matrix with zeros.
	[
		[0, 0, 0, 0, 0, 0], # row 1
		[0, 0, 0, 0, 0, 0], # row 2
		[0, 0, 0, 0, 0, 0], # row 3
		[0, 0, 0, 0, 0, 0], # row 4
		[0, 0, 0, 0, 0, 0], # row 5
		[0, 0, 0, 0, 0, 0], # row 6
		[0, 0, 0, 0, 0, 0]  # row 7
	]
	Randomly places mines to the PMineField.
	[
		[9, 0, 9, 0, 0, 0], # row 1
		[0, 0, 9, 9, 0, 0], # row 2
		[0, 0, 0, 0, 0, 0], # row 3
		[0, 9, 0, 0, 0, 0], # row 4
		[0, 0, 0, 0, 0, 9], # row 5
		[9, 0, 9, 0, 0, 0], # row 6
		[0, 0, 0, 0, 0, 0]  # row 7
	]
	"""
	rows = len(PMineField)
	cols = len(PMineField[0])
	mines_placed = 0
	
	while mines_placed < PMines:
		row = random.randint(0, rows - 1)
		col = random.randint(0, cols - 1)
		
		if PMineField[row][col] != 9:
			PMineField[row][col] = 9
			mines_placed = mines_placed + 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
	"""
	Expects 2d-matrix with mines layed:
	[
		[9, 0, 9, 0, 0, 0], # row 1
		[0, 0, 9, 9, 0, 0], # row 2
		[0, 0, 0, 0, 0, 0], # row 3
		[0, 9, 0, 0, 0, 0], # row 4
		[0, 0, 0, 0, 0, 9], # row 5
		[9, 0, 9, 0, 0, 0], # row 6
		[0, 0, 0, 0, 0, 0]  # row 7
	]

	Calculates nearby mines:
	[
		[9, 3, 9, 3, 1, 0], # row 1
		[1, 3, 9, 9, 1, 0], # row 2
		[1, 2, 3, 2, 1, 0], # row 3
		[1, 9, 1, 0, 1, 1], # row 4
		[2, 3, 2, 1, 1, 9], # row 5
		[9, 2, 9, 1, 1, 1], # row 6
		[1, 2, 1, 1, 0, 0]  # row 7
	]
	"""
	rows = len(PMineField)
	cols = len(PMineField[0])
	
	for row in range(rows):
		for col in range(cols):
			if PMineField[row][col] != 9:
				count = 0
				# Check all 8 surrounding cells
				for dr in [-1, 0, 1]:
					for dc in [-1, 0, 1]:
						if dr == 0 and dc == 0:
							continue
						check_row = row + dr
						check_col = col + dc
						if check_row >= 0 and check_row < rows and check_col >= 0 and check_col < cols:
							if PMineField[check_row][check_col] == 9:
								count = count + 1
				PMineField[row][col] = count

def generateMinefield(
		PMineField: list[list[int]],
		PRows: int,
		PCols: int,
		PMines: int) -> None:
	"""
	Takes empty "PMineField" list and amount of rows, columns and mines as parameters.
	1. Clear 2D-Matrix
	2. Initializes "PMineField" list with zeros using PRows and then PCols
		for i in range(PRows): # ...
			PMineField.append([])
			for _ in range(PCols):
				PMineField[i].append(0)
	3. Lay mines
	4. Calculate nearbys
	"""
	PMineField.clear()
	
	for i in range(PRows):
		PMineField.append([])
		for _ in range(PCols):
			PMineField[i].append(0)
	
	layMines(PMineField, PMines)
	calculateNearbys(PMineField)

def main() -> None:
	"""
	Create a menu-driven program where user can generate boards for the
	Minesweeper game.

	Option 1: Generate minesweeper board
		- Ask amount of rows, columns and mines
		- Create board and store into memory
	Option 2: Show generated board
	Option 3: Save board
		- Ask filename and save values in comma-separated format (see below).
	Option 0: Exit

	## Saved text file content start ##
	9,3,9,3,1,0
	1,3,9,9,1,0
	1,2,3,2,1,0
	1,9,1,0,1,1
	2,3,2,1,1,9
	9,2,9,1,1,1
	1,2,1,1,0,0
	## Saved text file content end ##

	Each line must end in newline character '\n'
	"""
	minefield = []
	
	print("Program starting.")
	
	while True:
		print("Options:")
		print("1 - Generate minesweeper board")
		print("2 - Show generated board")
		print("3 - Save generated board")
		print("0 - Exit")
		choice = input("Your choice: ")
		
		if choice == "1":
			rows = int(input("Insert rows: "))
			cols = int(input("Insert columns: "))
			mines = int(input("Insert mines: "))
			generateMinefield(minefield, rows, cols, mines)
			print()
		
		elif choice == "2":
			if len(minefield) == 0:
				print("No board generated yet.")
				print()
			else:
				for row in minefield:
					print(row)
				print()
		
		elif choice == "3":
			if len(minefield) == 0:
				print("No board generated yet.")
				print()
			else:
				filename = input("Insert filename: ")
				with open(filename, 'w') as f:
					for row in minefield:
						row_str = ','.join(str(cell) for cell in row)
						f.write(row_str + '\n')
				print()
		
		elif choice == "0":
			print("Exiting program.")
			print()
			break
		
		else:
			print("Invalid choice.")
			print()
	
	print("Program ending.")

main()
