import random

def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def get_cows_and_bulls(secret, guess):
    cows = sum(1 for i in range(4) if secret[i] == guess[i])
    bulls = sum(1 for i in range(4) if guess[i] in secret) - cows
    return cows, bulls

def is_valid_guess(guess):
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4

def play_game():
    secret_number = generate_number()
    attempts = 0

    print("Welcome to the Cows and Bulls Game!")
    print("I have generated a 4-digit number with unique digits. Try to guess it!")

    while True:
        guess = input("Enter a 4-digit number: ")

        if not is_valid_guess(guess):
            print("Invalid input! Please enter a 4-digit number with unique digits.")
            continue

        attempts += 1
        cows, bulls = get_cows_and_bulls(secret_number, guess)

        if cows == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        else:
            print(f"{cows} cows, {bulls} bulls")

if __name__ == "__main__":
    play_game()
