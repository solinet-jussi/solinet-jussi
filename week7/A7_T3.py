# Course task: A7_T3 - Timestamp analysis

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
   print('Reading file "{}".'.format(PFilename))
   # 0. Clear PRows list just in case
   PRows.clear()
   # 1. Open filehandle
   file = open(PFilename, "r")
   # 2. Read filehandle line-by-line
   first_line = True
   while True:
      line = file.readline()
      if len(line) == 0:
         break
      # 2.1. Skip first line (header row)
      if first_line:
         first_line = False
         continue
      # 2.2. Check if line is empty '\n'
      if line == '\n':
         continue
      # 2.3. Add non empty datarow without newline at the end.
      PRows.append(line.rstrip('\n'))
   # 3. Close filehandle
   file.close()
   return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
   print("Analysing timestamps.")
   # Append results to the PResults list
   # Initialise helper list
   WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
   # Iterate rows with i
   for i in range(len(PRows)):
      # Iterate WEEKDAYS with j
      for j in range(len(WEEKDAYS)):
         # Check if the row starts with the weekday name
         if PRows[i].startswith(WEEKDAYS[j]):
            # Count the day in proper place
            WeekdayTimestampAmount[j] += 1
   # Iterate WEEKDAYS with i and append the daily results
   for i in range(len(WEEKDAYS)):
      PResults.append(f" - {WEEKDAYS[i]} {WeekdayTimestampAmount[i]} stamps")
   # Clear the helper list
   WeekdayTimestampAmount.clear()
   return None

def displayResults(PResults: list[str]) -> None:
   print("Displaying results.")
   # Iterate results and print for the user
   print("### Timestamp analysis ###")
   for result in PResults:
      print(result)
   print("### Timestamp analysis ###")
   return None

def main() -> None:
   # 1. Initialise
   # 1.1. Initialise rows list
   rows: list[str] = []
   # 1.2. Initialise results list
   results: list[str] = []
   # 2. Operate
   print("Program starting.")
   # 2.1. Ask user to define filename
   filename = input("Insert filename: ")
   # 2.2. Read file
   readFile(filename, rows)
   # 2.3. Analyse rows
   analyseTimestamps(rows, results)
   # 2.4. Display results
   displayResults(results)
   # 3. Cleanup
   # 3.1. Clear lists
   rows.clear()
   results.clear()
   print("Program ending.")
   return None

if __name__ == "__main__":
   main()

