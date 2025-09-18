# Course task: A2_T5: String length and slicing

print("Program starting.")

# Get user input for the compound word to work with
compound_word = input("Enter a closed compound word: ")

# String analysis 
compound_word_length = len(compound_word)
compound_word_last_character = compound_word[-1]
compound_word_reversed = compound_word[::-1]

# Display the results
print(f"The word you inserted is \'{compound_word}\' and in reverse it is \'{compound_word_reversed}\'")
print(f"The entered word length is {compound_word_length}")
print(f"The last character is \'{compound_word_last_character}\'")

# Get user input for custom slicing parameters
starting_point = int(input("1) Enter the starting point: "))  # Starting index for slice
ending_point = int(input("2) Enter the ending point: "))     # Ending index for slice (exclusive)
step_size = int(input("3) Enter the step size: "))           # Step size for slice (how many characters to skip)

# Perform custom slicing
sliced_word = compound_word[starting_point:ending_point:step_size]
print(f"The word '{compound_word}' sliced to the defined substring is '{sliced_word}'")

print("Program ending.")