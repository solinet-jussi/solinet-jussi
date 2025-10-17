# Course task: A6_T5 Number analytics

def readFile(filename):
   file = open("datasets/" + filename, "r")
   numbers = []
   while True:
      line = file.readline()
      if line == "\n":
         continue
      if len(line) == 0:
         break
      numbers.append(int(line.strip()))
   file.close()
   
   return {
       "numbers": numbers
   }

def analyseNumbers(numbers):
   number_count = len(numbers["numbers"])
   numbers_sum = sum(numbers["numbers"])
   numbers_max = max(numbers["numbers"])
   numbers_average = "{:.2f}".format(numbers_sum / number_count)

   return {
       "number_count": number_count,
       "numbers_sum": numbers_sum,
       "numbers_max": numbers_max,
       "numbers_average": numbers_average
   }

def formatOutputToCSV(data):
   headers = "Count;Sum;Greatest;Average"
   values = f"{data['number_count']};{data['numbers_sum']};{data['numbers_max']};{data['numbers_average']}"
   return f"{headers}\n{values}"

def main():
   print("Program starting.")
   print("This program analyses a list of names from a file.")
   # filename = input("Insert filename: ")
   filename = "A6_T5_D3.txt"
   print(f'File "{filename}" results:')
   numbers = readFile(filename)
   #print(numbers)
   print("#### Number analysis - START ####")
   analyzed_numbers = analyseNumbers(numbers)
   #print(analyzed_numbers)
   print(formatOutputToCSV(analyzed_numbers))
   print("#### Number analysis - END ####")
   print("Program ending.")


if __name__ == "__main__":
   main()