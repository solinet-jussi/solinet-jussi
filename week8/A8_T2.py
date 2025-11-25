# Course task: A8_T2 Calculator
import json
import calculator_utils
add = calculator_utils.add
subtract = calculator_utils.subtract
multiply = calculator_utils.multiply
divide = calculator_utils.divide

print("Program starting.")

def menu():
	print("Options:")
	print("1 - Add")
	print("2 - Subtract")
	print("3 - Multiply")
	print("4 - Divide")
	print("0 - Exit")

def askChoice():
	choice = input("Your choice: ")
	return choice

def main():
	print("Program starting.")
	while True:
		menu()
		choice = askChoice()
		if choice == "1":
			result = add()
			data = json.loads(result)
			print(f"{data['num1']} + {data['num2']} = {data['sum']}")

		elif choice == "2":
			result = subtract()
			data = json.loads(result)
			print(f"{data['num1']} - {data['num2']} = {data['difference']}")
		elif choice == "3":
			result = multiply()
			data = json.loads(result)
			print(f"{data['num1']} * {data['num2']} = {data['product']}")
		elif choice == "4":
			result = divide()
			data = json.loads(result)
			print(f"{data['num1']} / {data['num2']} = {data['quotient']}")
		elif choice == "0":
			print("Exiting program.")
			exit()
		else:
			print("Unknown option!")

if __name__ == "__main__":
   main()