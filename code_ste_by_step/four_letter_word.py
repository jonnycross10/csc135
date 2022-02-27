#need four_letter_words.txt as a sample input

def four_letter_words(file):
    with open(file, "r") as f:
        lines = f.readline()
        lines = lines.split(" ")
        count = filter(lambda x: len(x) == 4, lines)
        return len(list(count))

four_letter_words("four_letter_words")