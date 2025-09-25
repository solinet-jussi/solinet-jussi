# Course task: A2_T2: Escape sequence and print parameters

print("Program starting.")

car_brand = input("Enter car brand: ")
car_model = input("Enter car model: ")

# Note: sep parameter is redundant here since we only have one argument per print()
# To follow the task instructions, we use sep even if it's redundant
print(f"Car brand is \"{car_brand}\"", sep=" ", end=" ")
print(f"and the model is \'{car_model}\'", sep="-", end=".\n")

print("Car details: " + car_brand, car_model, sep=" | ")
print('Car brand is "', car_brand, '"', sep='', end=' ')
print("and the model is '", car_model, "'.", sep='')

print("Program ending.")