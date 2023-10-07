import random
# computer has a no , guess a number , get a hint , guess again till you get it

upper_limit = int(input(f'How big should the guess be ?'))


def computer_guess():
    guess = int((1+upper_limit)/2)
    actual = 1
    while actual:
        actual = int(input(f"Is your guess {guess} or is it too high (press 1) or too low (press -1) or correct (0) "))
        if actual == 1 :
            guess = random.randint(1,guess-1)
        elif actual == -1 :
            guess = random.randint(guess+1,upper_limit)
        else:
            print(f"So the no was {guess}")
            break


def player_guess():
    actual = random.randint(1,upper_limit)
    guess = 0
    while guess != actual:
        guess = int(input(f'guess a number between 1 and {upper_limit}'))
        guess_check(guess,actual)
    return


def guess_check(guess,actual):
    if guess > actual :
        print('guess is larger than actual number')
    elif guess < actual :
        print('guess is bigger than actual number')
    else:
        print('guessed right {0}'.format(actual))
    return


computer_guess()




