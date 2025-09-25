# Course task: A3_T2: String comparisons

print("Program starting.")
print("String comparisons")

first_word = input("Insert first word: ")
character = input("Insert a character: ")

if character in first_word:
    print(f'Word "{first_word}" contains character "{character}"')
else:
    print(f'Word "{first_word}" doesn\'t contain character "{character}"')

second_word = input("Insert second word: ")

if second_word < first_word:
    print(f'The second word "{second_word}" is before the first word "{first_word}" alphabetically.')
elif second_word > first_word:
    print(f'The second word "{second_word}" is after the first word "{first_word}" alphabetically.')
else:
    print(f'The second word "{second_word}" is the same as the first word "{first_word}".')

print("Program ending.")
