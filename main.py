import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input('Guess a number netween 1 and {x}')
        print(guess)

guess(10)