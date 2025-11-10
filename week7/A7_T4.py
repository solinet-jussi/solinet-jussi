# Course task: A7_T4 - Timestamp dataclass

DELIMITER = ";"

class TIMESTAMP:
   pass

def readTimestamps(PFilename, PTimestamps):
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

def displayTimestamps(PTimestamps):
   print("Electricity usage:")
   # Iterate timestamps and print for the user
   for timestamp in PTimestamps:
      # Format hour as HH:MM
      hour_formatted = f"{timestamp.hour}:00"
      # Format price
      price_formatted = f"{timestamp.price:.2f}"
      # Format consumption
      consumption_formatted = f"{timestamp.consumption:.2f}"
      # Calculate total
      total = timestamp.price * timestamp.consumption
      # Format total
      total_formatted = f"{total:.2f}"
      # Print formatted line
      print(f" - {timestamp.weekday} {hour_formatted}, price {price_formatted}, consumption {consumption_formatted} kWh, total {total_formatted} €")
   return None

def main():
   # 1. Initialise
   # 1.1. Initialise timestamps list
   timestamps = []
   # 2. Operate
   print("Program starting.")
   # 2.1. Ask user to define filename
   filename = input("Insert filename: ")
   # 2.2. Read file
   readTimestamps(filename, timestamps)
   # 2.3. Display results
   displayTimestamps(timestamps)
   # 3. Cleanup
   # 3.1. Clear list
   timestamps.clear()
   print("Program ending.")
   return None

if __name__ == "__main__":
   main()

