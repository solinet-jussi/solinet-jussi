########################################################
# Task A9_T5
# Developer Jussi Mäkelä
# Date 2025-12-11
########################################################

def askIntByte(PPrompt: str) -> int:
	# Ask for input
	Feed = input(PPrompt)

	# TODO: Use try-except to:
	#   - Convert input to float and int
	#   - Raise an exception if input is not numeric
	#   - Raise an exception if input is not an integer
	#   - Raise an exception if input is not in the range 0–255

	# If all checks pass, return the integer value
	try:
		# Try to convert to float first to check if numeric
		float_val = float(Feed)
		
		# Check if it's an integer (no decimal part)
		if float_val != int(float_val):
			raise ValueError(f'"{Feed}" is non-numeric value.')
		
		# Convert to integer
		int_val = int(float_val)
		
		# Check range
		if int_val < 0 or int_val > 255:
			raise ValueError(f'Value "{Feed}" is out of the range 0-255.')
		
		return int_val
		
	except ValueError as e:
		raise
	except Exception:
		raise ValueError(f'"{Feed}" is non-numeric value.')

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
	# TODO: Return a hex string in the format "#rrggbb"
	# Use string formatting: "{:02x}"
	return f"#{PRed:02x}{PGreen:02x}{PBlue:02x}"

def main():
	print("Program starting.")

	# TODO: Use try-except here to:
	#   - Call askIntByte for red, green, and blue
	#   - Call createHex to get the hex color
	#   - Print RGB values, hex value, and binary (8-bit) values
	#   - If any exception occurs, print the error and a message like:
	#     "Couldn't perform the designed task due to the invalid input values."
	try:
		red = askIntByte("Insert red: ")
		green = askIntByte("Insert green: ")
		blue = askIntByte("Insert blue: ")
		
		# All values are valid, display RGB details
		hex_color = createHex(red, green, blue)
		print("RGB Details:")
		print(f"- Red {red}")
		print(f"- Green {green}")
		print(f"- Blue {blue}")
		print(f"- Hex {hex_color}")
		print(f"- R-byte(base-2): {red:08b}")
		print(f"- G-byte(base-2): {green:08b}")
		print(f"- B-byte(base-2): {blue:08b}")
		
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
