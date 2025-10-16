# Course task: A6_T2 Write text file

def main():
   print("Program starting.")
   first_name = input("Insert first name: ")
   last_name = input("Insert last name: ")
   filename = input("Insert filename: ")

   file = open("datasets/" + filename, "w")
   file.write(first_name + "\n")
   file.write(last_name + "\n")
   file.close()

   print("Program ending.")


if __name__ == "__main__":
   main()