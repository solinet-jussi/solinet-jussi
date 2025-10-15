# Course task: A5_T2 Pass argument

def frameWord(pword):
	word_length = len(pword) + 4
	word_frame = "*" * word_length + "\n"
	word_frame += "* " + pword + " *" + "\n"
	word_frame += "*" * word_length + "\n"
	return word_frame

def main():
	print("Program starting.")
	input_word = input("Insert a word: ")
	framed_word = frameWord(input_word)
	print()
	print(framed_word)
	print("Program ending.")
	return None

main()