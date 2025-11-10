# Course task: A7_T5 - Electricity consumption

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)
DELIMITER = ";"

class TIMESTAMP:
   pass

class DAY_USAGE:
   pass

def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
   print('Reading file "{}".'.format(PFilename))
   # 0. Clear PTimestamps list just in case
   PTimestamps.clear()
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
      # 2.3. Process non empty datarow
      row = line.rstrip('\n')               # Remove newline
      columns = row.split(DELIMITER)        # Splits the row into a list
      timestamp = TIMESTAMP()               # Create object
      timestamp.weekday = columns[0]        # Collect the first column
      timestamp.hour = columns[1]           # Collect the second column
      timestamp.consumption = float(columns[2])  # Collect the third column and convert datatype
      timestamp.price = float(columns[3])   # Collect the fourth column and convert datatype
      PTimestamps.append(timestamp)
      columns.clear()
   # 3. Close filehandle
   file.close()
   return None

def analyseDailyUsage(PTimestamps: list[TIMESTAMP], PDayUsage: list[DAY_USAGE]) -> None:
   print("Analysing timestamps.")
   # Initialise helper list for daily usage and cost
   for i in range(len(WEEKDAYS)):
      day_usage = DAY_USAGE()
      day_usage.weekday = WEEKDAYS[i]
      day_usage.usage = 0.0  # Gatherer variable for daily usage
      day_usage.cost = 0.0   # Gatherer variable for daily cost
      PDayUsage.append(day_usage)
   
   # Iterate timestamps
   for timestamp in PTimestamps:
      # Find the index of the weekday in WEEKDAYS
      for i in range(len(WEEKDAYS)):
         if timestamp.weekday == WEEKDAYS[i]:
            # Add consumption to daily usage (gatherer)
            PDayUsage[i].usage += timestamp.consumption
            # Calculate cost for this timestamp and add to daily cost (gatherer)
            timestamp_cost = timestamp.consumption * timestamp.price
            PDayUsage[i].cost += timestamp_cost
            break
   return None

def displayResults(PDayUsage: list[DAY_USAGE], PResults: list[str]) -> None:
   print("Displaying results.")
   # Iterate day usage and create result strings
   for day_usage in PDayUsage:
      # Format usage and cost
      usage_formatted = f"{day_usage.usage:.2f}"
      cost_formatted = f"{day_usage.cost:.2f}"
      # Create result string
      result = f" - {day_usage.weekday} usage {usage_formatted} kWh, cost {cost_formatted} €"
      PResults.append(result)
   
   # Print results
   print("### Electricity consumption summary ###")
   for result in PResults:
      print(result)
   print("### Electricity consumption summary ###")
   return None

def main() -> None:
   # 1. Initialise
   # 1.1. Initialise timestamps list
   timestamps: list[TIMESTAMP] = []
   # 1.2. Initialise analysis helper list
   day_usage: list[DAY_USAGE] = []
   # 1.3. Initialise results list
   results: list[str] = []
   # 2. Operate
   print("Program starting.")
   # 2.1. Ask user to define filename
   filename = input("Insert filename: ")
   # 2.2. Read file
   readTimestamps(filename, timestamps)
   # 2.3. Analyse timestamps
   analyseDailyUsage(timestamps, day_usage)
   # 2.4. Display results
   displayResults(day_usage, results)
   # 3. Cleanup
   # 3.1. Clear lists
   timestamps.clear()
   day_usage.clear()
   results.clear()
   print("Program ending.")
   return None

if __name__ == "__main__":
   main()

