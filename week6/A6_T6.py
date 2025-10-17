# Course task: A6_T6 Cipher message

# Alphabets used by helper functions
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

# Shift for ROT13 cipher
ROT13_SHIFT = 13

def shiftCharacter(ch, alphabet, shift=ROT13_SHIFT):
   if ch in alphabet:
      index_in_alphabet = alphabet.index(ch)
      shifted_index = (index_in_alphabet + shift) % 26
      return alphabet[shifted_index]
   return ch

def rot13(text):
   cipher = ""
   for char in text:
      if char.isalpha():
         # Choose the alphabet start based on case ('a' or 'A') and assign it to its corresponding ASCII code 
         if char.islower():
            ascii_code = ord('a')
         else:
            ascii_code = ord('A')

         # Convert character to 0-25 index within alphabet
         alphabet_index = ord(char) - ascii_code

         # Apply the shift and wrap around using modulo 26
         shifted_index = (alphabet_index + ROT13_SHIFT) % 26

         # Convert back to a character and append
         shifted_char = chr(ascii_code + shifted_index)
         cipher += shifted_char
      else:
         # If character is not a letter, append it to the cipher
         cipher += char
   return cipher

def writeFile(filename, content):
   file_handle = open(filename, 'w', encoding="UTF-8")
   file_handle.write(content)
   file_handle.close()

def askRows():
   print("Collecting plain text rows for ciphering.")
   rows = []
   while True:
      row = input("Insert row(empty stops): ")
      if row == "":
         break
      rows.append(row)
   return "\n".join(rows)

def main():
   print("Program starting.")

   content = askRows()

   print()
   print("#### Ciphered text ####")
   ciphered_content = rot13(content)
   print(ciphered_content)

   print("#### Ciphered text ####")
   filename = input("Insert filename to save: ")
   if filename == "":
      print("File name not defined.")
      print("Aborting save operation.")
   else:
      writeFile(filename, ciphered_content)
      print("Ciphered text saved!")

   print("Program ending.")

if __name__ == "__main__":
   main()
