# The secret number game

from random import randrange
secret = randrange(31)
guess = -1

while guess != secret:
    guess = int(input("Guess a number between 0 and 30: "))

    if guess == secret:
        print("Congratulations! You won!")
    else:
        print("Try again!")
