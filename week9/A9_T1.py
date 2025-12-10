########################################################
# Task A9_T1
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

def main():
	print("Program starting.")
	float_numbers = []
	
	while True:
		user_input = input("Insert a floating-point value (0 to stop): ")
		
		try:
			input_float = float(user_input)
			
			if input_float == 0:
				break
			
			float_numbers.append(input_float)
			
		except ValueError:
			print("Error! '{}' couldn't be converted to float.".format(user_input))
	
	total_sum = sum(float_numbers)
	print("Final sum is {:.2f}".format(total_sum))
	print("Program ending.")

if __name__ == "__main__":
	main()