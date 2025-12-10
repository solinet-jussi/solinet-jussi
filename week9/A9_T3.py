########################################################
# Task A9_T3
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

print("Program starting.")
filename = input("Insert filename: ")

try:
	file = open(filename, 'r')
	content = file.read()
	print(f"## {filename} ##")
	print(content, end='')
	print(f"## {filename} ##")
	file.close()  # Must manually close
except FileNotFoundError:
	print(f'Couldn\'t read file "{filename}".')
	exit(1)

print("Program ending.")
