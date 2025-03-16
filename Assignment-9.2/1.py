def write_words_to_file(filename):
    words = ["Hands", "Legs", "India", "Crow", "Rain"]
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + "\n")

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    return words

filename = "words.txt"
write_words_to_file(filename)
word_list = read_words_from_file(filename)

print("Words in the list:", word_list)
