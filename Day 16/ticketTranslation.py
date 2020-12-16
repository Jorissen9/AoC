def checkAndTrimDict(valueToRemoveFromAll, dictionary, fieldThatSent):
    for field, possibleValues in dictionary.items():
        if field != fieldThatSent:
            if valueToRemoveFromAll in possibleValues:
                possibleValues.remove(valueToRemoveFromAll)
                
                if len(possibleValues) == 1:
                    checkAndTrimDict(possibleValues[0], dictionary, field)

input = open("input.txt")

rules = {}
otherTickets = []

otherTicketsNext = False
nextIsMine = False
for line in input:
    strippedLine = line.strip()

    if strippedLine == "your ticket:":
        nextIsMine = True
    elif nextIsMine:
        myTicket = strippedLine.split(',')
        nextIsMine = False
    elif strippedLine == "nearby tickets:":
        otherTicketsNext = True
    elif otherTicketsNext:
        otherTickets.append(strippedLine.split(','))
    elif strippedLine != '':
        fieldAndValidRanges = strippedLine.split(':')
        field = fieldAndValidRanges[0].strip()
        validRanges = fieldAndValidRanges[1].strip().split(" or ")
        validRangeValueTuples = []
        for validRange in validRanges:
            validRangeValueTuples.append(validRange.split('-'))
        rules[field] = validRangeValueTuples

invalidValues = []
validTickets = []
for otherTicket in otherTickets:
    validTicket = True
    for value in otherTicket:
        intValue = int(value)
        valid = False
        for field, validRanges in rules.items():
            for validRange in validRanges:
                if intValue in range(int(validRange[0]), int(validRange[1]) + 1):
                    valid = True
                    break
        
        if not valid:
            validTicket = False
            invalidValues.append(intValue)

    if validTicket:
        validTickets.append(otherTicket)

totalSum = 0
for invalidValue in invalidValues:
    totalSum += invalidValue
print("Error rate: " + str(totalSum))

#Part 2
possiblePositions = {}
for field, validRanges in rules.items():
    possiblePositions[field] = []

for i in range(len(myTicket)):
    intValue = int(value)
    for field, validRanges in rules.items():
        for validRange in validRanges:
            if intValue in range(int(validRange[0]), int(validRange[1]) + 1):
                possiblePositions[field].append(i)
                break

for ticket in validTickets:
    possiblePositionsOtherTicket = {}
    for field, validRanges in rules.items():
        possiblePositionsOtherTicket[field] = []

    foundAll = True
    for i in range(len(ticket)):
        value = ticket[i]
        intValue = int(value)
        for field, validRanges in rules.items():
            if len(possiblePositions[field]) > 1:
                foundAll = False
                for validRange in validRanges:
                    if intValue in range(int(validRange[0]), int(validRange[1]) + 1):
                        possiblePositionsOtherTicket[field].append(i)
                        break
    
    if foundAll:
        break

    for field, possiblePositionValues in possiblePositions.items():
        if len(possiblePositionValues) > 1:
            for possiblePositionValue in possiblePositionValues:
                if possiblePositionValue not in possiblePositionsOtherTicket[field]:
                    possiblePositionValues.remove(possiblePositionValue)
                
                    if len(possiblePositionValues) == 1:
                        checkAndTrimDict(possiblePositionValues[0], possiblePositions, field)

print(possiblePositions)

finalString = ""
multDepartureStuff = 1
for field, position in possiblePositions.items():
    if field[:9] == "departure":
        multDepartureStuff *= int(myTicket[position[0]])
    finalString += field + ": " + myTicket[position[0]] + "\n"

print(finalString)
print("Departure multiplied: " + str(multDepartureStuff))