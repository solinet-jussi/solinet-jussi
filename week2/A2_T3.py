# Course task: A2_T3: String length and concatenation

print("Program starting.")

first_word = input("Enter first word: ")
second_word = input("Enter second word: ")

first_word_length = len(first_word)
second_word_length = len(second_word)

print(f"1st word is {first_word_length} characters long.")
print(f"2nd word is {second_word_length} characters long.")

concatenated_words = first_word + second_word
concatenated_words_length = len(concatenated_words)

print(f"Words together makes one closed compound \'{concatenated_words}\'")

print("Program ending.")
