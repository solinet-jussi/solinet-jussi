# Course task: A5_T7 Words in a string

DELIMITER = ","

def collectWords():
	words = []
	word = None
	while word != "":
		word = input("Insert word(empty stops): ")
		if word == "":
			break
		words.append(word)
	return DELIMITER.join(words)

def analyseWords(words_str):
	if words_str == "":
		word_list = []
	else:
		word_list = words_str.split(DELIMITER)
	word_count = len(word_list)
	character_count = sum(len(w) for w in word_list)
	average = 0 if word_count == 0 else character_count / word_count
	print(f"- {word_count} Words")
	print(f"- {character_count} Characters")
	print(f"- {average:.2f} Average word length")
	return None

def main():
	print("Program starting.")
	words_str = collectWords()
	analyseWords(words_str)
	print("Program ending.")
	return None

main()
