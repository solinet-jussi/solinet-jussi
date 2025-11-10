# Course task: A7_T7 - Enigma machine

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def readConfig(PFilename: str, PRotors: list[str], PReflector: list[str]) -> None:
   """Read Enigma configuration from a simple key:value file."""
   print('Reading file "{}".'.format(PFilename))
   with open(PFilename, "r") as file:
      for raw_line in file:
         line = raw_line.strip()
         if not line or ":" not in line:
            continue
         key, value = [part.strip() for part in line.split(":", 1)]
         if key == "Rotor1":
            PRotors[0] = value
         elif key == "Rotor2":
            PRotors[1] = value
         elif key == "Rotor3":
            PRotors[2] = value
         elif key == "Reflector":
            PReflector[0] = value
   return None

def rotateRotors(PPositions: list[int]) -> None:
   """Step the rotors once (rightmost first)."""
   PPositions[0] = (PPositions[0] + 1) % 26
   if PPositions[0] == 0:
      PPositions[1] = (PPositions[1] + 1) % 26
      if PPositions[1] == 0:
         PPositions[2] = (PPositions[2] + 1) % 26
   return None

def forwardPassThrough(PLetter: str, PRotors: list[str], PPositions: list[int]) -> str:
   """Run a letter forward through rotors 1 -> 3."""
   index = ALPHABET.index(PLetter)
   for i in range(3):
      rotor = PRotors[i]
      pos = PPositions[i]
      offset_idx = (index + pos) % 26
      offset_char = ALPHABET[offset_idx]
      rotor_pos = rotor.index(offset_char)  # inverse lookup
      index = (rotor_pos - pos) % 26
   return ALPHABET[index]

def reversePassThrough(PLetter: str, PRotors: list[str], PPositions: list[int]) -> str:
   """Run a letter backward through rotors 3 -> 1."""
   index = ALPHABET.index(PLetter)
   for i in range(2, -1, -1):
      rotor = PRotors[i]
      pos = PPositions[i]
      offset = (pos + index) % 26
      char_at_offset = rotor[offset]  # direct lookup
      char_idx = ALPHABET.index(char_at_offset)
      index = (char_idx - pos) % 26
   return ALPHABET[index]

def reflect(PLetter: str, PReflector: str) -> str:
   """Reflect a letter using the reflector wiring."""
   return PReflector[ALPHABET.index(PLetter)]

def processCharacter(PCharacter: str, PRotors: list[str], PReflector: list[str], PPositions: list[int]) -> str:
   """Encrypt/decrypt a single character."""
   if PCharacter.upper() not in ALPHABET:
      return PCharacter
   letter = PCharacter.upper()
   letter = forwardPassThrough(letter, PRotors, PPositions)
   letter = reflect(letter, PReflector[0])
   letter = reversePassThrough(letter, PRotors, PPositions)
   return letter

def processRow(PRow: str, PRotors: list[str], PReflector: list[str], PPositions: list[int]) -> str:
   """Process a whole line of text."""
   PPositions[0] = 0
   PPositions[1] = 0
   PPositions[2] = 0
   result = []
   for char in PRow:
      if char.upper() in ALPHABET:
         rotateRotors(PPositions)
         processed_char = processCharacter(char, PRotors, PReflector, PPositions)
      else:
         processed_char = char
      print('Character "{}" illuminated as "{}"'.format(char, processed_char))
      result.append(processed_char)
   return ''.join(result)

def main() -> None:
   """Main function to run Enigma machine."""
   rotors: list[str] = ["", "", ""]  # 3 rotors
   reflector: list[str] = [""]  # Reflector
   positions: list[int] = [0, 0, 0]  # Rotor positions
   config_filename = input("Insert config(filename): ")
   readConfig(config_filename, rotors, reflector)
   plug_choice = input("Insert plugs (y/n)?: ")
   if plug_choice.lower() == 'y':
      print("Plugboard implementation skipped.")
   else:
      print("No extra plugs inserted.")
   print("Enigma initialized.")
   print()
   while True:
      row = input("Insert row (empty stops): ")
      if row == "":
         break
      converted_row = processRow(row, rotors, reflector, positions)
      print('Converted row - "{}".'.format(converted_row))
      print()
   print("Enigma closing.")
   return None

if __name__ == "__main__":
   main()

