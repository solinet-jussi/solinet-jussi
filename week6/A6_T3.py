# Course task: A6_T3 Copy text file

def main():
   print("Program starting.")
   print("This program can copy a file.")
   source_filename = input("Insert source filename: ")
   destination_filename = input("Insert destination filename: ")
   
   print(f"Reading file '{source_filename}' content.")
   
   # Read from source file
   source_file = open("datasets/" + source_filename, "r")
   content = ""
   while True:
      line = source_file.readline()
      if len(line) == 0:
         break
      content += line
   source_file.close()
   
   print("File content ready in memory.")
   print(f"Writing content into file '{destination_filename}'.")
   
   # Write to destination file
   destination_file = open("datasets/" + destination_filename, "w")
   destination_file.write(content)
   destination_file.close()
   
   print("Copying operation complete.")
   print("Program ending.")


if __name__ == "__main__":
   main()
