# Course task: A6_T1 Read text file

def main():
   print("Program starting.")
   print("This program can read a file.")
   filename = input("Insert filename: ")

   print(f'#### START "{filename}" ####')

   file = open("datasets/" + filename, "r")
   while True:
      line = file.readline()
      if len(line) == 0:
         break
      print(line, end="")
   file.close()

   print()
   print(f'#### END "{filename}" ####')
   print("Program ending.")


if __name__ == "__main__":
   main()