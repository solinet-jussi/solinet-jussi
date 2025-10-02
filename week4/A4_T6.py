# Course task: A4_T6 Collatz Conjecture

print("Program starting.")

number = int(input("Insert a positive integer: "))
numbers = [number]

while number != 1:
    # If number is even, divide by 2
    if number % 2 == 0:
        number = number // 2
    # If number is odd, multiply by 3 and add 1
    else:
        number = 3 * number + 1
    numbers.append(number)

sequence_steps = len(numbers) - 1
i = 0

for number in numbers:

	if i == sequence_steps:
		print(number)
	else:
		print(number, end="->")

	i += 1

print(f"Sequence had {sequence_steps} total steps.")
print("\nProgram ending.")

