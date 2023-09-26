
# Analysing marks in Long Jump

# This version is refactored using functions
# Function for reading the marks of a player:
def read_marks(nameOfPlayer):
    """ Assumes 'nameOfPlayer' is a (non-empty) string.
        Reads integer numbers from input and builds a list
        with them until no input is given.
        Returns the resulting list of integer marks. """

    marksOfPlayer = []

    getNext = True
    while getNext:
        inputMark = input("Input a mark for player " + nameOfPlayer + ": ")
        if inputMark == '':  # if input is empty
            getNext = False
        elif 'x' in inputMark:  # if input contains x
            marksOfPlayer.append(None)
        else:                   # if itst not empty and doesnt contain x we asume its valid
            marksOfPlayer.append(int(inputMark))
            
    return marksOfPlayer

# Function for calculating the best mark of a player:


def find_best(marks):
    """ Assumes 'marks' is a list of integers.
        Returns None if list 'marks' is empty,
                or the highest number in it otherwise. """

    highest = None
    for mark in marks:
        if highest == None or mark > highest:
            highest = mark
        return highest

# Function for calculating the winner or winners,
# given their best marks:


def determine_winner(nameA, nameB, bestA, bestB):
    """ Assumes 'bestA' and 'bestB' are each either None or an integer.
        Returns a list possibly including each of 'nameA' and 'nameB'
                depending on the best marks between 'bestA' and 'bestB'. """

    if bestA == None:
        if bestB == None:
            winners = []
        else:
            winners = [nameB]
    else:
        if bestB == None:
            winners = [nameA]
        else:
            if bestA > bestB:
                winners = [nameA]
            elif bestA < bestB:
                winners = [nameB]
            else:
                winners = [nameA, nameB]

    return winners

# Function for outputting the winner or winners,
# if there are any:


def output_winner_result(namesOfWinners):
    """ Assumes 'namesOfWinners' is a list of strings.
        Returns nothing but prints a result. """

    if len(namesOfWinners) == 0:
        print("Nobody wins.")
    elif len(namesOfWinners) == 1:
        print("Player", namesOfWinners[0], "wins.")
    else:
        print("It is a tie between player", namesOfWinners[0],
              "and player", namesOfWinners[1] + ".")

# Main program:


# Read the marks for both player A and player B:
marksA = read_marks("A")
marksB = read_marks("B")
# Calculate the best mark for both player A and player B:
highestA = find_best(marksA)
highestB = find_best(marksB)
# Calculate the winners and output the result:
winners = determine_winner("A", "B", highestA, highestB)
output_winner_result(winners)
