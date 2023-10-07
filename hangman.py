## get a clean word , display the possible word, while displaying check if all
import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.lower()


# add guess and count no of guesses
def get_guess(word,guess_set,word_set,count):
    print("You have used these letter: "," ".join(guess_set))
    guess = input("Enter letter from a-z for guessing the word or Enter 0 to exit:")
    guess_set.add(guess)
    if guess not in word_set and guess not in guess_set:
        count += 1
    return guess_set , count


# display guess outcome
def display_word(word,guess_set,word_set):
    temp = [x if x in guess_set else "_" for x in word]
    [print(items,end="|") for items in temp]
    print()
    if word_set.issubset(guess_set):
        print("Congratulations! Game Completed")
        return 0
    else:
        print("take another guess")
        return 1


def hangman_play(words):
    word = get_valid_word(words)
    word_set = set(word)
    print(word)
    guess_set = set()
    count = 0
    while (display_word(word,guess_set,word_set)) and ("0" not in guess_set) and (count <= 6):
        # if words are guessed completely , display it else display rest
        guess_set,count = get_guess(word,guess_set, word_set,count)
    if count > 6 :
        print(f"Word was {word}")
        print("Game Lost")
    else:
        print("Game Closed")


if __name__  == "__main__":
    hangman_play(words)
