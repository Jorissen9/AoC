def getSeatsAroundIndex(ferrySeats, row, column):
    seatsAroundIndex = []
    rangeToCheck = [-1, 0, 1]
    for rowChange in rangeToCheck:
        rowToCheck = row + rowChange
        if 0 <= rowToCheck < len(ferrySeats):
            for columnChange in rangeToCheck:
                columnToCheck = column + columnChange
                if 0 <= columnToCheck < len(ferrySeats[0]) and not columnChange == rowChange == 0:
                    seatsAroundIndex.append(ferrySeats[rowToCheck][columnToCheck])
    return seatsAroundIndex

def executeRules(ferrySeatsInitial):
    ferrySeatsNew = []
    for row in range(len(ferrySeatsInitial)):
        rowString = ferrySeatsInitial[row]
        ferrySeatsNew.append(rowString)
        for column in range(len(rowString)):
            ferrySeat = rowString[column]
            if ferrySeat == 'L':
                if not '#' in getSeatsAroundIndex(ferrySeatsInitial, row, column):
                    ferrySeatsNew[row] = ferrySeatsNew[row][:column] + '#' + ferrySeatsNew[row][column + 1:]
            elif ferrySeat == '#':
                if getSeatsAroundIndex(ferrySeatsInitial, row, column).count('#') >= 4:
                    ferrySeatsNew[row] = ferrySeatsNew[row][:column] + 'L' + ferrySeatsNew[row][column + 1:]
    
    return ferrySeatsNew

def countCharInTable(table, char):
    total = 0
    for row in table:
        total += row.count(char)
    return total

#Part 2
def getSeatsAroundIndexWhatTheyCanSee(ferrySeats, row, column):
    seatsAroundIndex = []
    rangeToCheck = [-1, 0, 1]
    for rowChange in rangeToCheck:
        rowToCheck = row + rowChange
        if 0 <= rowToCheck < len(ferrySeats):
            for columnChange in rangeToCheck:
                columnToCheck = column + columnChange
                if 0 <= columnToCheck < len(ferrySeats[0]) and not columnChange == rowChange == 0:
                    #This Check Thingy only thing that's different
                    newRowToCheck = rowToCheck
                    newColumnToCheck = columnToCheck
                    checkedSoFarYouFellOfTheBoat = False
                    while not checkedSoFarYouFellOfTheBoat and ferrySeats[newRowToCheck][newColumnToCheck] == '.':
                        newRowToCheck += rowChange
                        newColumnToCheck += columnChange
                        if not (0 <= newRowToCheck < len(ferrySeats)) or not(0 <= newColumnToCheck < len(ferrySeats[0])):
                            checkedSoFarYouFellOfTheBoat = True

                    if not checkedSoFarYouFellOfTheBoat:
                        ###
                        seatsAroundIndex.append(ferrySeats[newRowToCheck][newColumnToCheck])
    return seatsAroundIndex

def executeRulesWhatTheyCanSee(ferrySeatsInitial):
    ferrySeatsNew = []
    for row in range(len(ferrySeatsInitial)):
        rowString = ferrySeatsInitial[row]
        ferrySeatsNew.append(rowString)
        for column in range(len(rowString)):
            ferrySeat = rowString[column]
            if ferrySeat == 'L':
                if not '#' in getSeatsAroundIndexWhatTheyCanSee(ferrySeatsInitial, row, column):
                    ferrySeatsNew[row] = ferrySeatsNew[row][:column] + '#' + ferrySeatsNew[row][column + 1:]
            elif ferrySeat == '#':
                if getSeatsAroundIndexWhatTheyCanSee(ferrySeatsInitial, row, column).count('#') >= 5: # that diff though
                    ferrySeatsNew[row] = ferrySeatsNew[row][:column] + 'L' + ferrySeatsNew[row][column + 1:]
    
    return ferrySeatsNew

# Both parts
ferrySeatsInitial = []
input = open("input.txt")

for line in input:
    ferrySeatsInitial.append(line.strip())

#Part 1
ferrySeats = ferrySeatsInitial
while True:
    ferrySeatsNew = executeRules(ferrySeats)
    if ferrySeatsNew == ferrySeats:
        break
    else:
        ferrySeats = ferrySeatsNew

print(countCharInTable(ferrySeatsNew, '#'))

#Part 2
ferrySeats = ferrySeatsInitial
while True:
    ferrySeatsNew = executeRulesWhatTheyCanSee(ferrySeats)
    if ferrySeatsNew == ferrySeats:
        break
    else:
        ferrySeats = ferrySeatsNew

print(countCharInTable(ferrySeatsNew, '#'))