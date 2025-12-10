########################################################
# Task A9_T4
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius(input_string):
	try:
		celsius = float(input_string)
	except ValueError:
		raise ValueError(f"could not convert string to float: '{input_string}'")
	
	if celsius < TEMP_MIN or celsius > TEMP_MAX:
		raise Exception(f"{celsius:.1f} temperature out of range.")
	
	return celsius

def main():
	print("Program starting.")
	user_input = input("Insert Celsius: ")
	
	try:
		celsius = collectCelsius(user_input)
		print(f"You inserted {celsius:.1f} °C")
	except ValueError as e:
		print(str(e))
	except Exception as e:
		print(str(e))
	
	print("Program ending.")

if __name__ == "__main__":
	main()
