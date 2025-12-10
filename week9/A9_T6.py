########################################################
# Task A9_T6
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

lines = []

def save_lines(filename):
    # Save lines to a file.
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def handle_keyboard_interrupt():
    # Handle keyboard interrupt based on whether there are unsaved lines.
    if len(lines) == 0:
        print("Closing suddenly.")
    else:
        print("Keyboard interrupt and unsaved progress!")
        response = input("Save before quit(y/n)?: ")
        if response.lower() == 'y':
            filename = input("Insert filename: ")
            save_lines(filename)

print("Program starting.")
try:
    while True:
        print("\nOptions:")
        print("1 - Insert line")
        print("2 - Save lines")
        print("0 - Exit")
        choice = input("Your choice: ")
        
        if choice == '1':
            text = input("Insert text: ")
            lines.append(text)
        elif choice == '2':
            filename = input("Insert filename: ")
            save_lines(filename)
        elif choice == '0':
            break
        else:
            print("Unknown option!")
            
except KeyboardInterrupt:
    handle_keyboard_interrupt()

print("Program ending.")
