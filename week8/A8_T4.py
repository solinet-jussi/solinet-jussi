# Course task: A8_T4 Years, Months and Weekdays

from datetime import datetime

MONTHS = (
	"January",
	"February",
	"March",
	"April",
	"May",
	"June",
	"July",
	"August",
	"September",
	"October",
	"November",
	"December"
)

WEEKDAYS = (
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
)

def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
	# Read timestamps from file and append to PTimestamps list.
	try:
		file = open(PFilename, "r")
		while True:
			line = file.readline()
			if len(line) == 0:
				break
			if line == "\n":
				continue
			line = line.strip()
			# Parse timestamp format: YYYY-MM-DDTHH:MM
			timestamp = datetime.strptime(line, "%Y-%m-%dT%H:%M")
			PTimestamps.append(timestamp)
		file.close()
	except FileNotFoundError:
		print(f"File '{PFilename}' not found.")
	except ValueError:
		print("Error parsing timestamp.")

def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
	# Calculate amount of timestamps during given year.
	count = 0
	for timestamp in PTimestamps:
		if timestamp.year == PYear:
			count += 1
	return count

def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
	# Calculate amount of timestamps during given month.
	count = 0
	# Find month index (1-12)
	month_index = -1
	for i in range(len(MONTHS)):
		if MONTHS[i] == PMonth:
			month_index = i + 1  # datetime.month is 1-based
			break
	
	if month_index == -1:
		return 0
	
	for timestamp in PTimestamps:
		if timestamp.month == month_index:
			count += 1
	return count

def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
	# Calculate amount of timestamps during given weekday.
	count = 0
	# Find weekday index (0=Monday, 6=Sunday)
	weekday_index = -1
	for i in range(len(WEEKDAYS)):
		if WEEKDAYS[i] == PWeekday:
			weekday_index = i  # datetime.weekday() returns 0=Monday, 6=Sunday
			break
	
	if weekday_index == -1:
		return 0
	
	for timestamp in PTimestamps:
		if timestamp.weekday() == weekday_index:
			count += 1
	return count

def display_menu():
	print("Options:")
	print("1 - Calculate amount of timestamps during year")
	print("2 - Calculate amount of timestamps during month")
	print("3 - Calculate amount of timestamps during weekday")
	print("0 - Exit")

def main():
	print("Program starting.")
	
	# Read filename and load timestamps
	filename = input("Insert filename: ")
	timestamps = []
	readTimestamps(filename, timestamps)
	
	if len(timestamps) == 0:
		print("No timestamps loaded.")
		print("Program ending.")
		return
	
	while True:
		display_menu()
		choice = input("Your choice: ")
		
		if choice == "1":
			try:
				year = int(input("Insert year: "))
				count = calculateYears(year, timestamps)
				print(f"Amount of timestamps during year '{year}' is {count}")
			except ValueError:
				print("Invalid year format.")
		elif choice == "2":
			month = input("Insert month: ")
			count = calculateMonths(month, timestamps)
			print(f"Amount of timestamps during month '{month}' is {count}")
		elif choice == "3":
			weekday = input("Insert weekday: ")
			count = calculateWeekdays(weekday, timestamps)
			print(f"Amount of timestamps during weekday '{weekday}' is {count}")
		elif choice == "0":
			print("Exiting program.")
			break
		else:
			print("Unknown option!")
	
	print("Program ending.")

if __name__ == "__main__":
	main()
