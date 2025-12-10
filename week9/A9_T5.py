########################################################
# Task A9_T5
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

def validate_rgb_value(value_str, color_name):
	try:
		# Try to convert to float first to check if numeric
		float_val = float(value_str)
		
		# Check if it's an integer (no decimal part)
		if float_val != int(float_val):
			raise ValueError(f'"{value_str}" is non-numeric value.')
		
		# Convert to integer
		int_val = int(float_val)
		
		# Check range
		if int_val < 0 or int_val > 255:
			raise ValueError(f'Value "{value_str}" is out of the range 0-255.')
		
		return int_val
		
	except ValueError as e:
		raise
	except Exception:
		raise ValueError(f'"{value_str}" is non-numeric value.')

def main():
	print("Program starting.")
	
	try:
		red_str = input("Insert red: ")
		red = validate_rgb_value(red_str, "red")
		
		green_str = input("Insert green: ")
		green = validate_rgb_value(green_str, "green")
		
		blue_str = input("Insert blue: ")
		blue = validate_rgb_value(blue_str, "blue")
		
		# All values are valid, display RGB details
		print("RGB Details:")
		print(f"- Red {red}")
		print(f"- Green {green}")
		print(f"- Blue {blue}")
		print(f"- Hex #{red:02x}{green:02x}{blue:02x}")
		
	except ValueError as e:
		# Print the specific error message
		print(str(e))
		# Print the general error message
		print("Couldn't perform the designed task due to the invalid input values.")
	except Exception:
		# Catch any other exceptions as invalid input
		print("Couldn't perform the designed task due to the invalid input values.")
	
	print("Program ending.")

if __name__ == "__main__":
	main()
