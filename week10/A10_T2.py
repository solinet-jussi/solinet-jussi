########################################################
# Task A10_T2
# Developer Jussi Mäkelä
# Date 2025-12-03
########################################################

import sys  # for possible exit on errors

def readValues(PFilename: str, PValues: list[int]) -> None:
    # Read values from file, filter empty rows, and convert to integers
    try:
        with open(PFilename, 'r') as file:
            for line in file:
                # Strip newline characters and whitespace
                stripped_line = line.strip()
                # Ignore empty rows
                if stripped_line:
                    # Convert to integer and add to list
                    value = int(stripped_line)
                    PValues.append(value)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Could not convert a value to integer in file '{PFilename}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    # Calculate the sum of all values
    Sum = 0
    for value in PValues:
        Sum = Sum + value
    return Sum

def productOfValues(PValues: list[int]) -> int:
    # Calculate the product of all values
    Product = 1
    for value in PValues:
        Product = Product * value
    return Product

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    # 2. Operate
    print("Program starting.")
    # 2.1 ask filename
    filename = input("Insert filename: ")
    # 2.2 read values
    readValues(filename, Values)
    # 2.3 calculate sum of values
    Sum = sumOfValues(Values)
    # 2.4 calculate product of values
    Product = productOfValues(Values)
    # 2.5 display results
    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(Product)
    print("# --- Product of numbers --- #")
    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
