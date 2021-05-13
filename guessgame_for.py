# The secret number game (for)

from random import randrange
secret = randrange(31)
guess = -1
max_try = 3

for x in range(max_try):
    print("You have " + str(max_try-x) + " more tries")
    guess = int(input("Guess the number between 0 and 30: "))

    if guess > secret:
        print("Try a lower number")
    elif guess < secret:
        print("Try an higher number")
    else:
        print("Congratulations! You won!")
        break
