# Course task: A3_T6: Submenu

def main():
    print("Program starting.")
    print("Welcome to the unit converter program!")
    print("Follow the menu instructions below.")
    print()
    
    while True:
        print("Options:")
        print("1 - Length")
        print("2 - Weight")
        print("0 - Exit")
        choice = input("Your choice: ")
        print()
        
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            length_menu()
        elif choice == "2":
            weight_menu()
        else:
            print("Unknown option.")
            print()
    
    print("Program ending.")

def length_menu():
    while True:
        print("Length options:")
        print("1 - Meters to kilometers")
        print("2 - Kilometers to meters")
        print("0 - Exit")
        choice = input("Your choice: ")
        print()
        
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            meters = float(input("Insert meters: "))
            kilometers = meters / 1000
            print(f"{meters:.1f} m is {kilometers:.1f} km")
            print()
        elif choice == "2":
            kilometers = float(input("Insert kilometers: "))
            meters = kilometers * 1000
            print(f"{kilometers:.1f} km is {meters:.1f} m")
            print()
        else:
            print("Unknown option.")
            print()

def weight_menu():
    while True:
        print("Weight options:")
        print("1 - Grams to pounds")
        print("2 - Pounds to grams")
        print("0 - Exit")
        choice = input("Your choice: ")
        print()
        
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            grams = float(input("Insert grams: "))
            pounds = grams / 453.6
            print(f"{grams:.1f} g is {pounds:.1f} lb")
            print()
        elif choice == "2":
            pounds = float(input("Insert pounds: "))
            grams = pounds * 453.6
            print(f"{pounds:.1f} lb is {grams:.1f} g")
            print()
        else:
            print("Unknown option.")
            print()

if __name__ == "__main__":
    main()
