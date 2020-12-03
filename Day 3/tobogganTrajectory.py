def checkMap(treeMap, right, down):
    finiteAmount = len(finiteTreeMap[0])
    amountOfTreesEncountered = 0
    position = 0
    for i in range(len(finiteTreeMap)):
        if i % down == 0:
            treeLine = finiteTreeMap[i]
            if treeLine[position] == '#':
                amountOfTreesEncountered += 1
            
            position += right
            if (position >= finiteAmount):
                position -= finiteAmount

    return amountOfTreesEncountered

def checkAndMultiply(treeMap, differentSlopes):
    result = 1
    for slope in differentSlopes:
        result *= checkMap(treeMap, slope[0], slope[1])

    return result

finiteTreeMap = []
input = open("input.txt")

for line in input:
    finiteTreeMap.append(line.strip())

# Part 1
print("Amount of trees: " + str(checkAndMultiply(finiteTreeMap, [[3, 1]])))

# Part 2
print("Amount of trees multiplied: " + str(checkAndMultiply(finiteTreeMap, [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]])))