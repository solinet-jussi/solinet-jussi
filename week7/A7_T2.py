# Course task: A7_T1 - Analyse separated values
import json

def main():
   print("Program starting.")
   values = input("Insert comma separated integers: ")
   result = processValues(values)
   output = json.loads(result)
   if output['count'] == 0:
      print("No values to analyse.")
   else:
      print(f"There are {output['count']} integers in the list.")
      print(f"Sum of the integers is {output['sum']} and it's {output['parity']}")
   print("Program ending.")

def processValues(values):
   valueList = values.split(",")
   valueCount = 0
   valueSum = 0
   valueParity = None
   for value in valueList:
      if not value.isdigit():
         print(f"Invalid value \'{value}\' detected.")
         continue
      valueSum += int(value)
      valueParity = "even" if valueSum % 2 == 0 else "odd"
      valueCount += 1
   result = {
      "count": valueCount,
      "sum": valueSum,
      "parity": valueParity
   }
   return json.dumps(result)

if __name__ == "__main__":
   main()
