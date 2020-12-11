numbers = []
input = open("input.txt")

for line in input:
    numbers.append(int(line))

numbers.sort()
currentJoltMax = 3
oneJoltDiffs = 0
threeJoltDiffs = 0
prevNumber = 0

onesAftherEachOther = 0
possibleChangeIndexes = []
for minNumber in numbers:
    difference = minNumber - prevNumber
    prevNumber = minNumber
    if difference == 1:
        oneJoltDiffs += 1
        onesAftherEachOther += 1
        if onesAftherEachOther >= 1:
            index = numbers.index(minNumber)
            if index + 1 < len(numbers) and numbers[index + 1] - minNumber == 1:
                possibleChangeIndexes.append(index)
    elif difference == 3:
        threeJoltDiffs += 1
        onesAftherEachOther = 0

    if minNumber <= currentJoltMax:
        currentJoltMax = minNumber + 3
    else:
        print("RIP")
        break
threeJoltDiffs += 1

print("1-jolt diffs times 3-jolt diffs: " + str(oneJoltDiffs * threeJoltDiffs))

def multiplyList(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def calcPermutations(group):
    amount = len(group)
    if amount <= 2:
        return 2 ** amount
    elif amount == 3:
        return (2 ** amount) - 1
    elif amount >= 4: # Not 100% sure, but removing this also works so never > 3 🤷‍♂️
        return (2 ** amount) - (1 + 2 ** (amount - 3))

def handlePossibleIndexChanges(possibleChangeIndexes):
    groups = []
    group = []
    group.append(possibleChangeIndexes[0])
    for index in possibleChangeIndexes[1:]:
        if group[len(group) - 1] + 1 == index:
            group.append(index)
        else:
            groups.append(group)
            group = []
            group.append(index)

    groups.append(group)

    result = 1
    for group in groups:
        result *= calcPermutations(group)
    return result

print("Amount of permutations: " + str(handlePossibleIndexChanges(possibleChangeIndexes)))
