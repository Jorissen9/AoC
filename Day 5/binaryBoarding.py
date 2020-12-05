def isCalculatedSeatIdCorrect(calcSeatId, plane):
    minusOnePresent = False
    plusOnePresent = False
    for row in range(amountOfRows):
        for column in range(amountOfColumns):
            seatId = plane[row][column]
            if seatId != None:
                if seatId - 1 == calcSeatId:
                    minusOnePresent = True
                elif seatId + 1 == calcSeatId:
                    plusOnePresent = True

    return minusOnePresent and plusOnePresent

input = open("input.txt")

amountOfRows = 128
amountOfColumns = 8
highestSeatId = 0

plane = [[None for y in range(amountOfColumns)] for x in range(amountOfRows)]

for line in input:
    boardingCode = line.strip()
    rowInfluencer = boardingCode[:-3]
    columnInfluencer = boardingCode[7:]

    maxRow = amountOfRows
    minRow = 0
    maxCol = amountOfColumns
    minCol = 0

    for char in rowInfluencer:
        if char == 'F':
            maxRow -= (maxRow - minRow) / 2
        if char == 'B':
            minRow += (maxRow - minRow) / 2
    
    for char in columnInfluencer:
        if char == 'L':
            maxCol -= (maxCol - minCol) / 2
        if char == 'R':
            minCol += (maxCol - minCol) / 2
    
    if maxRow - 1 == minRow and maxCol - 1 == minCol:
        seatId = minRow * 8 + minCol
        plane[int(minRow)][int(minCol)] = seatId
        if seatId > highestSeatId:
            highestSeatId = seatId
            

print("Highest seat id: " + str(highestSeatId))

#Part 2
for row in range(amountOfRows):
    for column in range(amountOfColumns):
        seatId = plane[row][column]
        if seatId == None:
            calcSeatId = row * 8 + column
            if isCalculatedSeatIdCorrect(calcSeatId, plane):
                print("Your seat id: " + str(calcSeatId))
                exit()