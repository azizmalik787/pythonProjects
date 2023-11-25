from words import words
import random
import string


def valid_word():
    word = random.choice(words)
    while True:
        if '-' not in word and ' ' not in word:
            return word


def hangman():
    word = valid_word().upper()
    letters_guessed = set()
    letters_to_guess = set(word)
    validator = set(string.ascii_uppercase)
    lives = 6

    while len(letters_to_guess) > 0 and lives > 0:
        print("Letters used: ", " ".join(letters_guessed))
        current_word = [letter if letter in letters_guessed else '_' for letter in word]
        print(f"Current Lives: {lives}, Current word: ", " ".join(current_word))
        letter = input("Guess the word: ").upper()
        if letter in validator - letters_guessed:
            if letter in letters_to_guess:
                letters_guessed.add(letter)
                letters_to_guess.remove(letter)

            else:
                # wrong word or word already in guessed word list
                letters_guessed.add(letter)
                lives -= 1

        elif letter in letters_guessed:
            print("You have already guessed the letter.")
        else:
            print("Invalid letter entered.")

    if lives == 0:
        print(f"You lost, the word was {word}")
    else:
        print("Congratulations You won!!!")


hangman()