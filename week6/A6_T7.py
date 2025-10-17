# Course task: A6_T7 Messages from the Four Emperors

# Reuse ROT13 logic similarly to A6_T6 
ROT13_SHIFT = 13

def rot13(text):
   cipher = ""
   for char in text:
      if char.isalpha():
         if char.islower():
            ascii_code = ord('a')
         else:
            ascii_code = ord('A')
         alphabet_index = ord(char) - ascii_code
         shifted_index = (alphabet_index + ROT13_SHIFT) % 26
         shifted_char = chr(ascii_code + shifted_index)
         cipher += shifted_char
      else:
         cipher += char
   return cipher


# Locations
LOCATIONS = [
   "home",
   "Galba's palace",
   "Otho's palace",
   "Vitellius' palace",
   "Vespasian's palace",
]

def ensure_progress_initialized():
   try:
      f = open("player_progress.txt", "r")
      f.close()
   except:
      f = open("player_progress.txt", "w")
      f.write("current_location;next_location;passphrase\n")
      f.write("0;1;qvfpvcyvar\n")
      f.close()

def read_last_progress_row():
   f = open("player_progress.txt", "r")
   lines = []
   while True:
      line = f.readline()
      if len(line) == 0:
         break
      lines.append(line.rstrip('\n'))
   f.close()
   data_lines = []
   i = 0
   for ln in lines:
      if i > 0 and ln.strip() != "":
         data_lines.append(ln)
      i = i + 1
   if len(data_lines) == 0:
      return 0, 1, ""
   last = data_lines[len(data_lines) - 1]
   parts = last.split(';')
   if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit():
      return int(parts[0]), int(parts[1]), parts[2]
   return 0, 1, ""

def append_line_to_progress(line):
   f = open("player_progress.txt", "a")
   if line.endswith("\n"):
      f.write(line)
   else:
      f.write(line + "\n")
   f.close()

def read_message_lines(next_id, pass_ciphered):
   fname = str(next_id) + "_" + pass_ciphered + ".gkg"
   try:
      f = open(fname, "r")
      lines = f.readlines()
      f.close()
      return lines
   except:
      return []

def process_palace_message(next_id, pass_ciphered):
   pass_plain = rot13(pass_ciphered)
   print("Looking for the message in the palace...")
   
   lines = read_message_lines(next_id, pass_ciphered)
   print("Ah, there it is! Seems cryptic.")
   
   if len(lines) == 0:
      print("[Game] Progress autosaved!")
      print("Deciphering Emperor's message...")
      print("Looks like I've got now the plain version copy of the Emperor's message.")
      return

   append_line_to_progress(lines[0])
   print("[Game] Progress autosaved!")

   body_ciphered = ""
   i = 0
   for line in lines:
      if i > 0:
         body_ciphered = body_ciphered + line
      i = i + 1
   body_plain = rot13(body_ciphered)

   out_name = str(next_id) + "-" + pass_plain + ".txt"
   out = open(out_name, "w")
   out.write(body_plain)
   out.close()

   print("Deciphering Emperor's message...")
   print("Looks like I've got now the plain version copy of the Emperor's message.")


def main():
   ensure_progress_initialized()

   print("Travel starting.")

   current_id, next_id, pass_ciphered = read_last_progress_row()

   current_name = LOCATIONS[current_id] if 0 <= current_id < len(LOCATIONS) else "home"
   print("Currently at " + current_name + ".")

   if next_id >= len(LOCATIONS):
      print("Time to leave...")
      print("Travel ending.")
      return

   next_name = LOCATIONS[next_id]
   print("Travelling to " + next_name + "...")
   print("...Arriving to the " + next_name + ".")
   print("Passing the guard at the entrance.")

   pass_plain = rot13(pass_ciphered)
   print('"' + pass_plain + '"')

   process_palace_message(next_id, pass_ciphered)

   print("Time to leave...")
   print("Travel ending.")


if __name__ == "__main__":
   main()


