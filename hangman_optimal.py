from words import words
import random
import string


def get_valid_word():
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word


def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    while len(word_letters) > 0:
        # print words used
        print('you have used these letters ',', '.join(used_letter))
        # Print words left
        guess_state = [letter if letter in used_letter else "-" for letter in word]
        print(' word so far : ',' '.join(guess_state))
        print(word_letters)
        # Take Input
        user_input = input("guess a letter: ").upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

        elif user_input in used_letter:
            print("Already guessed this no")

        else:
            print("invalid characters")


if __name__  == "__main__":
    hangman()