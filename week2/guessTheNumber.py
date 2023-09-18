import random
randomNumber = random.randint(0, 100)
gameRepeat = "Y"
bestScore = 10000
numberOfAttempts = 0

while gameRepeat == "Y":
    numberOfAttempts = numberOfAttempts + 1

    userNumber = int(input("Guess a number between 1 and 100: "))
    if userNumber > 100 or userNumber < 0:
        print("Please enter a number in the range! ")
    else:
        if userNumber == randomNumber:
            print("Correct! :>")
            print("It took you " + str(numberOfAttempts) + " attempts")
            if numberOfAttempts < bestScore:
                bestScore = numberOfAttempts
            print("Best score so far is: " + str(bestScore))
            numberOfAttempts = 0
            randomNumber = random.randint(0, 100)
            gameRepeat = input("Wanna play again? ( Y or N): ")
        else:
            if userNumber > randomNumber:
                print("Go lower")
            else:
                print("Go higher")
