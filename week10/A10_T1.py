########################################################
# Task A10_T1
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

print("Program starting.")
filename = input("Insert filename: ")

# Read the file and collect non-empty lines
values = []
with open(filename, 'r') as file:
    for line in file:
        # Strip newline characters and whitespace
        stripped_line = line.strip()
        # Ignore empty rows
        if stripped_line:
         	values.append(stripped_line)

# Display vertically
print("# --- Vertically --- #")
for value in values:
    print(value)
print("# --- Vertically --- #")

# Display horizontally
print("# --- Horizontally --- #")
horizontal_output = ", ".join(values)
print(horizontal_output)
print("# --- Horizontally --- #")

print("Program ending.")
