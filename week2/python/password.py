password = "Banana"
counter = 0
correctCheck = False
while counter < 3 and correctCheck == False:
    userInput = input("Enter your password: ")
    if userInput == password:
        correctCheck = True

    else:
        print("Incorrect, try again ")
    counter = counter + 1

if correctCheck == True:
    print("Correct password! ")
else:
    print("You used all your tries. Game Over!")
