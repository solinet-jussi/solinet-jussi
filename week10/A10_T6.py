########################################################
# Task A10_T6
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

import copy
import time
from typing import Callable

def readValues(PValues: list[int|float]) -> str:
	# clear values list to ensure no duplicate data (reading twice)
	PValues.clear()
	
	# get filename from user
	filename = input("Insert dataset filename: ")
	
	# open filehandle
	try:
		filehandle = open(filename, 'r')
		# read line-by-line
		for line in filehandle:
			# parse value(int) from line(str + '\n')
			stripped_line = line.strip()
			# ignore empty lines
			if stripped_line:
				value = int(stripped_line)
				# append value into the values list
				PValues.append(value)
		# close filehandle
		filehandle.close()
	except FileNotFoundError:
		print(f"Error: File '{filename}' not found.")
	except ValueError:
		print(f"Error: Could not convert a value to integer in file '{filename}'.")
	except Exception as e:
		print(f"Error reading file: {e}")
	
	return filename

def quickSort(PNums: list[int]) -> list[int]:
	# https://en.wikipedia.org/wiki/Quicksort
	# Base case: if list has 0 or 1 element, it's already sorted
	if len(PNums) <= 1:
		return PNums
	
	# Choose pivot (first element)
	pivot = PNums[0]
	
	# Partition into three lists: less than pivot, equal to pivot, greater than pivot
	less = []
	equal = []
	greater = []
	
	for num in PNums:
		if num < pivot:
			less.append(num)
		elif num == pivot:
			equal.append(num)
		else:
			greater.append(num)
	
	# Recursively sort less and greater, then combine
	return quickSort(less) + equal + quickSort(greater)

def bubbleSort(PNums: list[int]) -> list[int]:
	# https://en.wikipedia.org/wiki/Bubble_sort
	# Create a copy to avoid modifying the original
	result = PNums.copy()
	n = len(result)
	
	# Outer loop: number of passes
	for i in range(n):
		# Inner loop: compare adjacent elements
		for j in range(0, n - i - 1):
			# If current element is greater than next, swap them
			if result[j] > result[j + 1]:
				# Swap elements
				temp = result[j]
				result[j] = result[j + 1]
				result[j + 1] = temp
	
	return result

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
	StartTime = time.perf_counter_ns()
	PSortingAlgorithm(PArr) # param is function
	EndTime = time.perf_counter_ns()
	ElapsedTime = EndTime - StartTime
	return ElapsedTime

def main() -> None:
	# 1. Initialize
	Values: list[int] = []
	Results: list[str] = []
	DatasetFilename: str = ""
	BuiltinSortedTimeNs: int = 0
	BubbleSortTimeNs: int = 0
	QuickSortTimeNs: int = 0
	
	# 2. Operate
	print("Program starting.")
	
	# Menu loop
	while True:
		print("Options:")
		print("1 - Read dataset values")
		print("2 - Measure speeds")
		print("3 - Save results")
		print("0 - Exit")
		choice = input("Your choice: ")
		
		if choice == "1":
			# Read dataset values
			DatasetFilename = readValues(Values)
		
		elif choice == "2":
			# Measure speeds
			if not Values:
				print("Error: Please read dataset values first (option 1).")
				continue
			
			if not DatasetFilename:
				print("Error: No dataset loaded.")
				continue
			
			# pass algorithm into the measureSortingTime function # import copy
			BuiltinSortedTimeNs = measureSortingTime(sorted, copy.deepcopy(Values))
			BubbleSortTimeNs = measureSortingTime(bubbleSort, copy.deepcopy(Values))
			QuickSortTimeNs = measureSortingTime(quickSort, copy.deepcopy(Values))
			
			# Display results
			print(f"Measured speeds for dataset '{DatasetFilename}':")
			print(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
			print(f" - Bubble sort {BubbleSortTimeNs} ns")
			print(f" - Quick sort {QuickSortTimeNs} ns")
		
		elif choice == "3":
			# Save results
			if BuiltinSortedTimeNs == 0 and BubbleSortTimeNs == 0 and QuickSortTimeNs == 0:
				print("Error: Please measure speeds first (option 2).")
				continue
			
			if not DatasetFilename:
				print("Error: No dataset filename available.")
				continue
			
			results_filename = input("Insert results filename: ")
			
			# Build results list
			Results.clear()
			Results.append(f"Measured speeds for dataset '{DatasetFilename}':")
			Results.append(f" - Built-in sorted {BuiltinSortedTimeNs} ns")
			Results.append(f" - Bubble sort {BubbleSortTimeNs} ns")
			Results.append(f" - Quick sort {QuickSortTimeNs} ns")
			
			# Write to file
			try:
				filehandle = open(results_filename, 'w')
				for line in Results:
					filehandle.write(line + "\n")
				filehandle.close()
			except Exception as e:
				print(f"Error saving results: {e}")
		
		elif choice == "0":
			# Exit
			print("Exiting program.")
			break
		
		else:
			print("Invalid choice. Please try again.")
	
	# 3. Cleanup
	Values.clear()
	Results.clear()
	print("Program ending.")
	return None

if __name__ == "__main__":
	main()
