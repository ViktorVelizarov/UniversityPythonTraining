choice = "Y"

while choice == "Y":

    N = int(input("enter N: "))

    while N >= 9:
        if N == 9:
            N = int(input("9 is not a valid number, try again: "))
        else:
            N = int(input("Please enter a number lower than 10: "))

    computerNum = N+1
    print("My number is " + str(computerNum) + " so I WIN!")

    choice = str(input("Want to play again? (Y or N)"))

print("Game Over!")
