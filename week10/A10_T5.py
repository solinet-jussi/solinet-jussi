########################################################
# Task A10_T5
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

def recursiveFactorial(PNum: int) -> int:
	# Base case: factorial of 0 or 1 is 1
	if PNum <= 1:
		return 1
	# Recursive case: n! = n * (n-1)!
	return PNum * recursiveFactorial(PNum - 1)

def buildFactorialString(PNum: int) -> str:
	# Build the string representation: 1*2*3*...*n
	if PNum <= 0:
		return ""
	if PNum == 1:
		return "1"
	# Recursively build the string
	prev_string = buildFactorialString(PNum - 1)
	return prev_string + "*" + str(PNum)

def main() -> None:
	print("Program starting.")
	
	# Get factorial number from user
	factorial_input = input("Insert factorial: ")
	factorial_num = int(factorial_input)
	
	# Calculate factorial recursively
	result = recursiveFactorial(factorial_num)
	
	# Build the calculation string
	calc_string = buildFactorialString(factorial_num)
	
	# Display the result
	print(f"Factorial {factorial_num}!")
	print(f"{calc_string} = {result}")
	print("Program ending.")
	
	return None

if __name__ == "__main__":
	main()
