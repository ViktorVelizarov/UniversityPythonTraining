
def average_segment(numbers, start, end):
    sum = 0
    for x in range(start, end):
        sum = numbers[x] + sum
    avg = sum / 7
    return avg


def printWeeks(measurmentsList):
    if (len(measurmentsList) < 7):  # check if there are enough measurments to make a week average
        print("\nNo week averages")
    else:
        # check how many week averages we can create
        numOfWeeks = len(measurmentsList) // 7
        startNum = 0
        endNum = 7
        print("\n")
        for x in range(1, numOfWeeks+1):
            weekReport = average_segment(measurmentsList, startNum, endNum)
            print("The average for week " + str(x) + " is: " + str(weekReport))
            startNum = startNum + 7
            endNum = endNum + 7


def printMonths(measurmentsList):
    if (len(measurmentsList) < 30):  # check if there are enough measurments to make a month average
        print("\nNo month averages")
    else:
        # check how many month averages we can create
        numOfMonths = len(measurmentsList) // 30
        startNum = 0
        endNum = 30
        print("\n")
        for x in range(1, numOfMonths+1):
            monthReport = average_segment(measurmentsList, startNum, endNum)
            print("The average for month " +
                  str(x) + " is: " + str(monthReport))
            startNum = startNum + 30
            endNum = endNum + 30


def outputReport():
    measurmentsList = input_numbers()
    print("\n__________________________________________________")
    print("The total average is: " +
          str(average_segment(measurmentsList, 0, len(measurmentsList))))
    printWeeks(measurmentsList)
    printMonths(measurmentsList)
    print("__________________________________________________")


def input_numbers():
    inputList = []
    checkInput = True
    print("\n__________________________________________________")
    while checkInput == True:
        userInput = input("add item: ")
        if userInput:  # check if the user input is empty
            inputList.append(float(userInput))
        else:
            # if the user input is empty, we stop the while cycle so he can't input anymore
            checkInput = False
    return inputList


rainfall = [0.6, 0.5, 3, 0, 0, 1.4]
# get the returned list from input_numbers() and set it as a list parameter in average()
outputReport()
