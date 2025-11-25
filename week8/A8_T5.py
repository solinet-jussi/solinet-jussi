# Course task: A8_T5 Login and register

import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def hash_password(password):
	# Hash password using MD5 and return hexdigest string.
	return hashlib.md5(password.encode()).hexdigest()

def read_credentials():
	# Read all credentials from file and return as list of tuples (id, username, hashed_password).
	credentials = []
	try:
		file = open(CREDENTIALS_FILE, "r")
		while True:
			line = file.readline()
			if len(line) == 0:
				break
			if line == "\n":
				continue
			line = line.strip()
			parts = line.split(DELIMITER)
			if len(parts) == 3:
				credentials.append((parts[0], parts[1], parts[2]))
		file.close()
	except FileNotFoundError:
		# File doesn't exist yet, return empty list
		pass
	return credentials

def write_credentials(credentials):
	# Write all credentials to file.
	file = open(CREDENTIALS_FILE, "w")
	for cred in credentials:
		file.write(f"{cred[0]}{DELIMITER}{cred[1]}{DELIMITER}{cred[2]}\n")
	file.close()

def get_next_id(credentials):
	# Get the next available ID for a new user.
	if len(credentials) == 0:
		return 0
	max_id = -1
	for cred in credentials:
		try:
			user_id = int(cred[0])
			if user_id > max_id:
				max_id = user_id
		except ValueError:
			continue
	return max_id + 1

def register_user():
	# Register a new user.
	username = input("Insert username: ")
	password = input("Insert password: ")
	
	credentials = read_credentials()
	user_id = get_next_id(credentials)
	hashed_password = hash_password(password)
	
	credentials.append((str(user_id), username, hashed_password))
	write_credentials(credentials)
	
	print("User registration completed!")

def login_user():
	# Attempt to login a user. Returns (success, user_id, username) tuple.
	username = input("Insert username: ")
	password = input("Insert password: ")
	
	hashed_password = hash_password(password)
	credentials = read_credentials()
	
	for cred in credentials:
		if cred[1] == username and cred[2] == hashed_password:
			return (True, cred[0], cred[1])
	
	return (False, None, None)

def display_main_menu():
	# Display main menu options.
	print("Options:")
	print("1 - Login")
	print("2 - Register")
	print("0 - Exit")

def display_user_menu():
	# Display user menu options.
	print("User menu:")
	print("1 - View profile")
	print("2 - Change password")
	print("0 - Logout")

def handle_user_menu(user_id, username):
	# Handle user menu interactions.
	while True:
		display_user_menu()
		choice = input("Your choice: ")
		
		if choice == "1":
			print(f"Profile ID {user_id} - {username}")
		elif choice == "2":
			# Change password not required to implement
			pass
		elif choice == "0":
			print("Logging out...")
			break
		else:
			print("Unknown option!")

def main():
	# Main program loop.
	print("Program starting.")
	
	while True:
		display_main_menu()
		choice = input("Your choice: ")
		
		if choice == "1":
			success, user_id, username = login_user()
			if success:
				print("Authentication successful!")
				handle_user_menu(user_id, username)
			else:
				print("Authentication failed!")
		elif choice == "2":
			register_user()
		elif choice == "0":
			print("Exiting program.")
			break
		else:
			print("Unknown option!")
	
	print("Program ending.")

if __name__ == "__main__":
	main()

