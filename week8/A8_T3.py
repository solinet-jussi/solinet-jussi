# Course task: A8_T3 Number files

def readFile(filename):
	readFile = open(filename, "r")
	lines = []
	# Skip empty lines
	while True:
		line = readFile.readline()
		if line == "\n":
			continue
		if len(line) == 0:
			break
		lines.append(line.strip())

	readFile.close()
	return lines

def analyseFile(data, option):
	# Read values
	if option == "1":
		return data

	# Amount of values
	elif option == "2":
		return len(data)
	
	# Sum of values
	elif option == "3":
		total = 0
		for value in data:
			if value != "":
				try:
					total += float(value)
				except ValueError:
					continue
		return total

	# Average of values
	elif option == "4":
		average = 0
		for value in data:
			if value != "":
				try:
					average += float(value)
				except ValueError:
					continue
		return average / len(data)

def menu():
	print("Options:")
	print("1 - Read values")
	print("2 - Amount of values")
	print("3 - Sum of values")
	print("4 - Average of values")
	return input("Your choice: ")

if __name__ == "__main__":
	fileName = "A8_T3_D2.txt"
	data = readFile(fileName)
	while True:
		option = menu()
		if option == "1":
			data = readFile(fileName)
			result = round(analyseFile(data, option), 1)
			print(f"Values: {result}")
		elif option == "2":
			result = round(analyseFile(data, option), 1)
			print(f"Amount of values: {result}")
		elif option == "3":
			result = round(analyseFile(data, option), 1)
			print(f"Sum of values: {result}")
		elif option == "4":
			result = round(analyseFile(data, option), 1)
			print(f"Average of values: {result}")
		elif option == "0":
			print("Exiting...")
			exit()
		else:
			print("Unknown option!")