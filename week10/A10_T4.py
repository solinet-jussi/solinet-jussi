########################################################
# Task A10_T4
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
	# Merge two sorted lists into PMerge
	# Clear PMerge first to ensure it's empty
	PMerge.clear()
	
	# Indexes for left and right lists
	left_index = 0
	right_index = 0
	
	# Compare and merge elements from both lists
	while left_index < len(PLeft) and right_index < len(PRight):
		if PAsc:
			# Ascending order: take smaller element
			if PLeft[left_index] <= PRight[right_index]:
				PMerge.append(PLeft[left_index])
				left_index = left_index + 1
			else:
				# Append right element
				PMerge.append(PRight[right_index])
				right_index = right_index + 1
		else:
			# Descending order: take larger element
			if PLeft[left_index] >= PRight[right_index]:
				PMerge.append(PLeft[left_index])
				left_index = left_index + 1
			else:
				PMerge.append(PRight[right_index])
				right_index = right_index + 1
	
	# Append remaining elements from left list
	while left_index < len(PLeft):
		PMerge.append(PLeft[left_index])
		left_index = left_index + 1
	
	# Append remaining elements from right list
	while right_index < len(PRight):
		PMerge.append(PRight[right_index])
		right_index = right_index + 1
	
	return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
	# Sort PValues using merge sort algorithm
	# PAsc: in ascending order by default. False will sort in descending order.
	
	# Base case: if list has 0 or 1 element, it's already sorted
	if len(PValues) <= 1:
		return None
	
	# Find the middle point
	mid = len(PValues) // 2
	
	# Split into left and right halves
	left = PValues[0:mid]
	right = PValues[mid:]
	
	# Recursively sort both halves
	mergeSort(left, PAsc)
	mergeSort(right, PAsc)
	
	# Merge the sorted halves back into PValues
	merge(left, right, PValues, PAsc)
	
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
	mergeSort(ValuesAsc, True)
	asc_output = ", ".join(str(v) for v in ValuesAsc)
	print(f"Ascending '{filename}' -> {asc_output}")
	
	# Sort descending
	ValuesDesc = Values.copy()
	mergeSort(ValuesDesc, False)
	desc_output = ", ".join(str(v) for v in ValuesDesc)
	print(f"Descending '{filename}' -> {desc_output}")
	
	return None

if __name__ == "__main__":
	main()
