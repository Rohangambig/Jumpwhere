import random

def write_words_to_file(filename):
    words = ["Hands", "Legs", "India", "Crow", "Rain", "Tree", "House", "Cloud", "River", "Mountain"]
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + "\n")

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    return words

def choose_random_word(word_list):
    return random.choice(word_list)

def play_hangman(word):
    guessed_letters = set()
    attempts = 6
    word_display = ['_' for _ in word]
    
    print("Welcome to Hangman!")
    print(' '.join(word_display))
    
    while attempts > 0 and '_' in word_display:
        guess = input("Guess your letter: ").upper()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print(f"Incorrect! You left with {attempts} chances to guess.")
        
        print(' '.join(word_display))
    
    if '_' not in word_display:
        print("Congratulations! You guessed the word correctly.")
    else:
        print(f"Game over! The word was {word}.")

def main():
    filename = "words.txt"
    write_words_to_file(filename)
    words = read_words_from_file(filename)
    random_word = choose_random_word(words).upper()
    play_hangman(random_word)

if __name__ == "__main__":
    main()
