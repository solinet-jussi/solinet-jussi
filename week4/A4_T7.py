# Course task: A4_T7 Multiplicative persistency

print("Program starting.")
print("\nCheck the multiplicative persistence.")
number = int(input("Insert an integer: "))
step_count = 0

def calculate_product(number):
	exploded_number = [int(digit) for digit in str(number)]
	product = 1

	for i in range(len(exploded_number)):
		digit = exploded_number[i]
		product *= digit
	return product

def print_multiplication_formula(number):
	exploded_number = [int(digit) for digit in str(number)]
	product = 1
	
	# Print the multiplication formula
	for i in range(len(exploded_number)):
		digit = exploded_number[i]
		product *= digit
		if i == len(exploded_number) - 1:
			print(f"{digit} = {product}")
		else:
			print(digit, end=" * ")

while True:
	print_multiplication_formula(number)
	number = calculate_product(number)
	step_count += 1
	if number < 10:
		print("No more steps.")
		print(f"This program took {step_count} step(s)")
		break

print("\nProgram ending.")

