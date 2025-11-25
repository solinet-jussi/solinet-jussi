# Course task: A8_T1 Pause
import time

print("Program starting.")


def menu():
	print("Options:")
	print("1 - Set pause duration")
	print("2 - Activate pause")
	print("0 - Exit")
	choice = input("Your choice: ")
	return choice


def setPauseDuration():
	duration = float(input("Insert pause duration (s): "))
	return duration


def activatePause(duration):
	print(f"Pausing for {duration} seconds...")
	time.sleep(duration)
	print("Unpaused.")


def main():
	print("Program starting.")
	duration = None
	while True:
		choice = menu()
		if choice == "1":
			duration = setPauseDuration()
		elif choice == "2":
			if duration is not None:
				activatePause(duration)
			else:
				print("Set a pause duration first.")
				exit()
		elif choice == "0":
			print("Exiting...")
			exit()
		else:
			print("Unknown option!")

if __name__ == "__main__":
   main()