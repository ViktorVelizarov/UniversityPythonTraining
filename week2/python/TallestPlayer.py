playerDictionary = {}
biggestHeight = 0
tallestPlayer = ""
for x in range(0, 3):
    print("Whats the name of player " + str(x+1))
    playerName = input()
    print("Whats the height of player " + str(x+1))
    playerHeight = input()
    playerDictionary[playerName] = playerHeight

for playerName, playerHeight in playerDictionary.items():
    if int(playerHeight) > int(biggestHeight):
        biggestHeight = playerHeight
        tallestPlayer = playerName
print(str(tallestPlayer) + " is the highest player with height: " + str(biggestHeight))
