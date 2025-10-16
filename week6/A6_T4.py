# Course task: A6_T1 Read text file

def analyse_names(filename):
   file = open("datasets/" + filename, "r")
   names = []
   while True:
      line = file.readline()
      if (line == "\n"):
         continue
      if len(line) == 0:
         break
      names.append(line.strip())
   file.close()
   name_count = len(names)
   shortest_name = len(min(names, key=len))
   longest_name = len(max(names, key=len))
   average_name_length = "{:.2f}".format(sum(len(name) for name in names) / name_count)

   return {
       "name_count": name_count,
       "shortest_name": shortest_name,
       "longest_name": longest_name,
       "average_name_length": average_name_length
   }

def main():
   print("Program starting.")
   print("This program analyses a list of names from a file.")
   filename = input("Insert filename to read: ")
   #filename = "A6_T4_D3.txt"
   print(f'Reading names from "{filename}".')
   print("Analysing names...")

   names = analyse_names(filename)
   print("Analysis complete.")
   print("#### REPORT BEGIN ####")
   print(f'Name count: {names["name_count"]}')
   print(f'Shortest name: {names["shortest_name"]} chars')
   print(f'Longest name: {names["longest_name"]} chars')
   print(f'Average name length: {names["average_name_length"]} chars')
   print("#### REPORT END ####")

   print("Program ending.")


if __name__ == "__main__":
   main()