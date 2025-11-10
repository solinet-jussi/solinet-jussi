# Course task: A7_T1 - Positive Integer Collector

def main():
   print("Program starting.")
   print("Collect positive integers.")

   numberList = collectPositiveIntegers()
   print("Stopped collecting positive integers.")
   
   listAllIntegers(numberList)
   print("Program ending.")

def collectPositiveIntegers():
   numberList = []
   while True:
      number = int(input("Insert a positive integer (negative stops): "))
      if number < 0:
         break
      numberList.append(number)
   return numberList

def listAllIntegers(numberList):
   if len(numberList) == 0:
      print("No integers to display.")
   else:
      print(f"Displaying {len(numberList)} integers:")
      for i in range(len(numberList)):
         print(f"- Index {i} => Ordinal {i+1} => Integer {numberList[i]}")

if __name__ == "__main__":
    main()
