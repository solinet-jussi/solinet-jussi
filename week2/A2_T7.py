# Course task: A2_T7: Fahrenheit to Celcius

print("Program starting.")

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
fahrenheit_rounded = round(fahrenheit, 1)
celcius = round((fahrenheit_rounded - 32) / 1.8, 1)
print(f"{fahrenheit_rounded}°F is {celcius}°C")
print("Program ending.")