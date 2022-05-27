import random


#you guess computers number
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number netween 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, too low!')
#         elif guess > random_number:
#             print('Guess again, sucka. Too high.')


#     print(f'Yo YOU GUESSED THE RIGHT NUMBER! IT WAS {random_number} !')


#computer guesses your number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high cuz low = high
        feedback = input(f'Is {guess} too high (M), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'YA THE COMPUTER GUESSED YOUR NUMBER! IT WAS {guess}!')

computer_guess(1000)