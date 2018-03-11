import random

def guess_check(the_number, guess):
    while guess != the_number:
        if guess > the_number:
            guess = int(input("Please, guess lower: "))
            continue
        if guess < the_number:
            guess = int(input("Please, guess higher: "))
            continue
    else:
        print("Congrads! You've guessed it!")


the_number = random.randint(1, 10)
guess = int(input('Please guess a number 1 to 10: '))


guess_check(the_number, guess)
