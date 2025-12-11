########################################################
# Task A10_T3
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

import sys

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
	# Sort PValues by implementing bubble sort algorithm.
	# Handle PValues list like it is a pointer to memory
	# Sort the list inplace e.g., PValues[CurrentIndex] = PValues[NextIndex]
	# Don't overwrite PValues identifier.
	# Tester expects that the PValues list is modified.
	# It doesn't catch a return value.
	
	n = len(PValues)
	
	# Outer loop for iterations
	for iteration in range(n):
		# Inner loop for comparisons
		# Compare up to n - iteration - 1 to avoid out-of-bounds
		for j in range(n - iteration - 1):
			# For ascending order: swap if current > next
			# For descending order: swap if current < next
			if PAsc:
				if PValues[j] > PValues[j + 1]:
					# Swap elements
					temp = PValues[j]
					PValues[j] = PValues[j + 1]
					PValues[j + 1] = temp
			else:
				if PValues[j] < PValues[j + 1]:
					# Swap elements
					temp = PValues[j]
					PValues[j] = PValues[j + 1]
					PValues[j + 1] = temp
	
	return None

def readValues(PFilename: str, PValues: list[int]) -> None:
	# Read values from file, filter empty rows, and convert to integers
	try:
		with open(PFilename, 'r') as file:
			for line in file:
				# Strip newline characters and whitespace
				stripped_line = line.strip()
				# Ignore empty rows
				if stripped_line:
					# Convert to integer and add to list
					value = int(stripped_line)
					PValues.append(value)
	except FileNotFoundError:
		print(f"Error: File '{PFilename}' not found.")
		sys.exit(1)
	except ValueError:
		print(f"Error: Could not convert a value to integer in file '{PFilename}'.")
		sys.exit(1)
	except Exception as e:
		print(f"Error reading file: {e}")
		sys.exit(1)
	return None

def main() -> None:
	print("Program starting.")
	
	# Handle CLI arguments or prompt for filename
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		print(f"The filename '{filename}' was passed via CLI.")
	else:
		filename = input("Insert filename: ")
	
	# Read values from file
	Values: list[int] = []
	readValues(filename, Values)
	
	# Display raw values
	raw_output = ", ".join(str(v) for v in Values)
	print(f"Raw '{filename}' -> {raw_output}")
	
	# Sort ascending
	ValuesAsc = Values.copy()
	bubbleSort(ValuesAsc, True)
	asc_output = ", ".join(str(v) for v in ValuesAsc)
	print(f"Ascending '{filename}' -> {asc_output}")
	
	# Sort descending
	ValuesDesc = Values.copy()
	bubbleSort(ValuesDesc, False)
	desc_output = ", ".join(str(v) for v in ValuesDesc)
	print(f"Descending '{filename}' -> {desc_output}")
	
	return None

if __name__ == "__main__":
	main()
