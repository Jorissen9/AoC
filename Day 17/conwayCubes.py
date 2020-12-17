inactiveChar = '.'
activeChar = '#'

def getActiveCubesAroundIndex(referenceCube, z, row, column):
    cubesAroundIndex = []
    rangeToCheck = [-1, 0, 1]
    for zChange in rangeToCheck:
        zToCheck = z + zChange
        if min(referenceCube.keys()) <= zToCheck <= max(referenceCube.keys()):
            for rowChange in rangeToCheck:
                rowToCheck = row + rowChange
                if min(referenceCube[zToCheck].keys()) <= rowToCheck <= max(referenceCube[zToCheck].keys()):
                    for columnChange in rangeToCheck:
                        columnToCheck = column + columnChange
                        if min(referenceCube[zToCheck][rowToCheck].keys()) <= columnToCheck <= max(referenceCube[zToCheck][rowToCheck].keys()) and not zChange == rowChange == columnChange == 0:
                            cubesAroundIndex.append(referenceCube[zToCheck][rowToCheck][columnToCheck])
    return cubesAroundIndex

def createNewSurface(refSurface):
    newSurface = {}
    for rowNumber, row in refSurface.items():
        flatRowOfCubes = {}
        for column in row.keys():
            flatRowOfCubes[column] = inactiveChar
        newSurface[rowNumber] = flatRowOfCubes
    return newSurface

def handleFlatSurface(z, initialSurface, referenceCube):
    newSurface = {}
    for row in range(min(referenceCube[0].keys()) - 1, max(referenceCube[0].keys()) + 2):
        flatRowOfCubes = {}
        for column in range(min(referenceCube[0][0].keys()) - 1, max(referenceCube[0][0].keys()) + 2):
            activeCubesAroundIndex = getActiveCubesAroundIndex(referenceCube, z, row, column)
            if min(referenceCube[0].keys()) <= row <= max(referenceCube[0].keys()) and min(referenceCube[0][row].keys()) <= column <= max(referenceCube[0][row].keys()):
                char = initialSurface[row][column]
            else:
                char = inactiveChar
            amountOfActiveCharsAroundIndex = activeCubesAroundIndex.count(activeChar)
            if char == activeChar:
                if 2 <= amountOfActiveCharsAroundIndex <= 3:
                    flatRowOfCubes[column] = activeChar
                else:
                    flatRowOfCubes[column] = inactiveChar
            elif char == inactiveChar:
                if amountOfActiveCharsAroundIndex == 3:
                    flatRowOfCubes[column] = activeChar
                else:
                    flatRowOfCubes[column] = inactiveChar
        newSurface[row] = flatRowOfCubes
    return newSurface

def executeRules(currentCube):
    newCube = {}
    for z, surface in currentCube.items():
        newSurface = handleFlatSurface(z, surface, currentCube)
        newCube[z] = newSurface

        previousZ = z - 1
        if previousZ not in currentCube.keys():
            prevZSurface = createNewSurface(surface)
            newPrevZSurface = handleFlatSurface(previousZ, prevZSurface, currentCube)
            newCube[previousZ] = newPrevZSurface
        
        nextZ = z + 1
        if nextZ not in currentCube.keys():
            nextZSurface = createNewSurface(surface)
            newNextZSurface = handleFlatSurface(nextZ, nextZSurface, currentCube)
            newCube[nextZ] = newNextZSurface
    return newCube

def countCharInCube(infiniteCubes, searchedChar):
    totalSum = 0
    for z, flatRegion in infiniteCubes.items():
        # print("Region: " + str(z))
        for flatLine in flatRegion.values():
            # print(flatLine)
            for flatChar in flatLine.values():
                if flatChar == searchedChar:
                    totalSum += 1
    return totalSum

input = open("input.txt")

x = -1
flatRegionOfCubes = {}
for line in input:
    y = -1
    flatRowOfCubes = {}
    for char in line.strip():
        flatRowOfCubes[y] = char
        y += 1
    flatRegionOfCubes[x] = flatRowOfCubes
    x += 1
infiniteCubes = {}
infiniteCubes[0] = flatRegionOfCubes
input.close()

#Part 1
for i in range(6):
    infiniteCubes = executeRules(infiniteCubes)

print(countCharInCube(infiniteCubes, activeChar))

#Part 2
def getActiveCubesAroundIndexHyper(referenceHyperCube, w, z, row, column):
    cubesAroundIndex = []
    rangeToCheck = [-1, 0, 1]
    for wChange in rangeToCheck:
        wToCheck = w + wChange
        if min(referenceHyperCube.keys()) <= wToCheck <= max(referenceHyperCube.keys()):
            for zChange in rangeToCheck:
                zToCheck = z + zChange
                if min(referenceHyperCube[wToCheck].keys()) <= zToCheck <= max(referenceHyperCube[wToCheck].keys()):
                    for rowChange in rangeToCheck:
                        rowToCheck = row + rowChange
                        if min(referenceHyperCube[wToCheck][zToCheck].keys()) <= rowToCheck <= max(referenceHyperCube[wToCheck][zToCheck].keys()):
                            for columnChange in rangeToCheck:
                                columnToCheck = column + columnChange
                                if min(referenceHyperCube[wToCheck][zToCheck][rowToCheck].keys()) <= columnToCheck <= max(referenceHyperCube[wToCheck][zToCheck][rowToCheck].keys()) and not wChange == zChange == rowChange == columnChange == 0:
                                    cubesAroundIndex.append(referenceHyperCube[wToCheck][zToCheck][rowToCheck][columnToCheck])
    return cubesAroundIndex

def handleFlatSurfaceHyper(w, z, initialSurface, referenceCube, referenceHyperCube):
    newSurface = {}
    for row in range(min(referenceCube[0].keys()) - 1, max(referenceCube[0].keys()) + 2):
        flatRowOfCubes = {}
        for column in range(min(referenceCube[0][0].keys()) - 1, max(referenceCube[0][0].keys()) + 2):
            activeCubesAroundIndex = getActiveCubesAroundIndexHyper(referenceHyperCube, w, z, row, column)
            if min(referenceCube[0].keys()) <= row <= max(referenceCube[0].keys()) and min(referenceCube[0][row].keys()) <= column <= max(referenceCube[0][row].keys()):
                char = initialSurface[row][column]
            else:
                char = inactiveChar
            amountOfActiveCharsAroundIndex = activeCubesAroundIndex.count(activeChar)
            if char == activeChar:
                if 2 <= amountOfActiveCharsAroundIndex <= 3:
                    flatRowOfCubes[column] = activeChar
                else:
                    flatRowOfCubes[column] = inactiveChar
            elif char == inactiveChar:
                if amountOfActiveCharsAroundIndex == 3:
                    flatRowOfCubes[column] = activeChar
                else:
                    flatRowOfCubes[column] = inactiveChar
        newSurface[row] = flatRowOfCubes
    return newSurface

def handleInfiniteCube(w, initialCube, refHyperCube):
    newCube = {}
    for z, surface in initialCube.items():
        newSurface = handleFlatSurfaceHyper(w, z, surface, initialCube, refHyperCube)
        newCube[z] = newSurface

        previousZ = z - 1
        if previousZ not in initialCube.keys():
            prevZSurface = createNewSurface(surface)
            newPrevZSurface = handleFlatSurfaceHyper(w, previousZ, prevZSurface, initialCube, refHyperCube)
            newCube[previousZ] = newPrevZSurface
        
        nextZ = z + 1
        if nextZ not in initialCube.keys():
            nextZSurface = createNewSurface(surface)
            newNextZSurface = handleFlatSurfaceHyper(w, nextZ, nextZSurface, initialCube, refHyperCube)
            newCube[nextZ] = newNextZSurface
    return newCube

def createNewInfiniteCube(infiniteCube):
    newCube = {}
    for z, surface in infiniteCube.items():
        newSurface = createNewSurface(surface)
        newCube[z] = newSurface
    return newCube


def executeHyperRules(currentHyperCube):
    newHyperCube = {}
    for w, infiniteCube in currentHyperCube.items():
        newInfiniteCube = handleInfiniteCube(w, infiniteCube, currentHyperCube)
        newHyperCube[w] = newInfiniteCube
        
        previousW = w - 1
        if previousW not in infiniteCube.keys():
            prevZCube = createNewInfiniteCube(infiniteCube)
            newPrevZCube = handleInfiniteCube(previousW, prevZCube, currentHyperCube)
            newHyperCube[previousW] = newPrevZCube
        
        nextW = w + 1
        if nextW not in infiniteCube.keys():
            nextZCube = createNewInfiniteCube(infiniteCube)
            newNextZCube = handleInfiniteCube(nextW, nextZCube, currentHyperCube)
            newHyperCube[nextW] = newNextZCube
        
    return newHyperCube

def countCharInHyperCube(hyperCubes, searchedChar):
    totalSum = 0
    for w, infiniteCubes in hyperCubes.items():
        for z, flatRegion in infiniteCubes.items():
            #print("Region: " + str(z) + " " + str(w))
            for flatLine in flatRegion.values():
                #print(flatLine)
                for flatChar in flatLine.values():
                    if flatChar == searchedChar:
                        totalSum += 1
    return totalSum

input = open("input.txt")

x = -1
flatRegionOfCubes = {}
for line in input:
    y = -1
    flatRowOfCubes = {}
    for char in line.strip():
        flatRowOfCubes[y] = char
        y += 1
    flatRegionOfCubes[x] = flatRowOfCubes
    x += 1
infiniteCubes = {}
infiniteCubes[0] = flatRegionOfCubes
hyperCubes = {}
hyperCubes[0] = infiniteCubes
input.close()

for i in range(6):
    hyperCubes = executeHyperRules(hyperCubes)

print(countCharInHyperCube(hyperCubes, activeChar))