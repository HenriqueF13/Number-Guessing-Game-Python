# Game highscore inside a file

# The secret number game

from random import randrange
secret = randrange(31)
guess = -1
tries = 0

with open("highscore.txt", "r") as myfile:
    topscore = int(myfile.read())
    print("The gold medal has " + str(topscore) + " points")

while True:
    tries = tries + 1
    print("Lets do the try number " + str(tries))
    guess = int(input("Guess the number between 0 and 30: "))

    if guess > secret:
        print("Try a lower number")
    elif guess < secret:
        print("Try an higher number")
    else:
        print("Congratulations! You won!")
        if tries < topscore:
            with open("highscore.txt", "w") as myfile:
                myfile.write(str(tries))
        break
