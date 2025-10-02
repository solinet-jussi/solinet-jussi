# Course task: A4_T4 Repetitive prompt

print("Program starting.")

words = []
word = None

while word != "":
    word = input("Enter a word (empty stops): ")
    if word == "":
        break
    words.append(word)

word_count = len(words)
char_count = 0
for word in words:
    char_count += len(word)

print("You entered:")
print(f"– {word_count} words")
print(f"– {char_count} characters")

print("Program ending.")
