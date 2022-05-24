import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number netween 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low!')
        elif guess > random_number:
            print('Guess again, sucka. Too high.')


    print('Yo YOU GUESSED THE RIGHT NUMBER! IT WAS {random_number}!')

guess(10)