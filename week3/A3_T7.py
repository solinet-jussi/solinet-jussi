# Course task: A3_T7: Decision trees

def run():
    print("Program starting.")
    print("Testing decision structures.")

    value_str = input("Insert an integer: ")
    try:
        value = int(value_str)
    except ValueError:
        # If non-integer is provided, treat as 0 per typical simple tasks or could raise.
        # The specification assumes an integer; we'll default to 0 to keep program running.
        value = 0

    print("Options:")
    print("1 - In one multi-branched decision")
    print("2 - In multiple independent if-statements")
    print("0 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        print("Using one multi-branched decision structure.")
        result = value
        if result >= 400:
            result += 44
        elif result >= 200:
            result += 22
        elif result >= 100:
            result += 11
        print(f"Result is {result}")
        print()
    elif choice == "2":
        print("Using multiple independent if-statements structure.")
        result = value
        if result >= 400:
            result += 44
        if result >= 200:
            result += 22
        if result >= 100:
            result += 11
        print(f"Result is {result}")
        print()
    elif choice == "0":
        print("Exiting...")
        print()
    else:
        print("Unknown option.")
        print()

    print("Program ending.")


if __name__ == "__main__":
    run()
