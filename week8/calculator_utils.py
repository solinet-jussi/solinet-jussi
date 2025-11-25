# simple calculator functions
import json

def add():
	num1 = float(input("Insert first addend value: "))
	num2 = float(input("Insert second addend value: "))
	result = num1 + num2
	return json.dumps({"num1": num1, "num2": num2, "sum": result})

def subtract():
	num1 = float(input("Insert minuend value: "))
	num2 = float(input("Insert subtrahend value: "))
	result = num1 - num2
	return json.dumps({"num1": num1, "num2": num2, "difference": result})

def multiply():
	num1 = float(input("Insert multiplicand value: "))
	num2 = float(input("Insert multiplier value: "))
	result = num1 * num2
	return json.dumps({"num1": num1, "num2": num2, "product": result})

def divide():
	num1 = float(input("Insert dividend value: "))
	num2 = float(input("Insert divisor value: "))
	result = num1 / num2
	return json.dumps({"num1": num1, "num2": num2, "quotient": result})
