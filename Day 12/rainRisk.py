completeRoute = []
input = open("input.txt")

for line in input:
    completeRoute.append(line.strip())

possibleDirections = ['E', 'N', 'W', 'S']

currentDirection = 0
currentEastValue = 0
currentNorthValue = 0

currentWaypointDirection = 0
currentWaypointEastValue = 10
currentWaypointNorthValue = 1
for direction in completeRoute:
    action = direction[:1]
    value = int(direction[1:])

    if action == "N":
        currentNorthValue += value
    elif action == "S":
        currentNorthValue -= value
    elif action == "E":
        currentEastValue += value
    elif action == "W":
        currentEastValue -= value
    elif action == "L":
        amountInArray = value // 90
        currentDirection = (currentDirection + amountInArray) % len(possibleDirections)
    elif action == "R":
        amountInArray = value // 90
        currentDirection = (currentDirection - amountInArray) % len(possibleDirections)
    elif action == "F":
        directionToGo = possibleDirections[currentDirection]
        if directionToGo == "N":
            currentNorthValue += value
        elif directionToGo == "S":
            currentNorthValue -= value
        elif directionToGo == "E":
            currentEastValue += value
        elif directionToGo == "W":
            currentEastValue -= value
        
print("Manhattan distance: " + str(abs(currentEastValue) + abs(currentNorthValue)))

#Part 2
currentShipEastValue = 0
currentShipNorthValue = 0

currentWaypointEastValue = 10
currentWaypointNorthValue = 1
for direction in completeRoute:
    action = direction[:1]
    value = int(direction[1:])

    if action == "N":
        currentWaypointNorthValue += value
    elif action == "S":
        currentWaypointNorthValue -= value
    elif action == "E":
        currentWaypointEastValue += value
    elif action == "W":
        currentWaypointEastValue -= value
    elif action == "L":
        amountToMove = value // 90
        for i in range(amountToMove):
            helpMePls = currentWaypointNorthValue
            currentWaypointNorthValue = currentWaypointEastValue
            currentWaypointEastValue = -helpMePls
    elif action == "R":
        amountToMove = value // 90
        for i in range(amountToMove):
            helpMePls = currentWaypointNorthValue
            currentWaypointNorthValue = -currentWaypointEastValue
            currentWaypointEastValue = helpMePls
    elif action == "F":
        currentShipEastValue += value * currentWaypointEastValue
        currentShipNorthValue += value * currentWaypointNorthValue

print("Manhattan distance: " + str(abs(currentShipEastValue) + abs(currentShipNorthValue)))
