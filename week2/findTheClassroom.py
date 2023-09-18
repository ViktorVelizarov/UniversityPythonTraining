roomNumbers = {
    "Math": "100",
    "English": "200",
    "Biology": "300",
    "History": "400",
    "PE": "500"
}

studentName = input("Enter your name: ")
studentSubject = input("What subject are you studying: ")

if studentSubject in roomNumbers:
    print("Hi " + studentName + ", go to room number "
          + roomNumbers[studentSubject] + " for " + studentSubject)
else:
    print("I don't know which room that class is in :/")
