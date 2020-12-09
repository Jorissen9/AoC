def isValid(numbers, requestedSum):
    for number in numbers:
        for number2 in numbers:
            if number + number2 == requestedSum:
                return True
    return False

def findEncyptionWeakness(numbers, startIndex, invalidNumber):
    i = startIndex
    totalSum = 0
    totalSumList = []
    while i < len(numbers):
        number = int(numbers[i])
        totalSum += number
        if totalSum > invalidNumber:
            totalSumList = findEncyptionWeakness(numbers, startIndex + 1, invalidNumber)
            break
        elif totalSum == invalidNumber:
            totalSumList.append(number)
            return totalSumList
        else:
            totalSumList.append(number)
            i += 1

    return totalSumList

numbers = []
input = open("input.txt")

for line in input:
    numbers.append(int(line))

preambleLen = 25
preamble = numbers[:preambleLen]
changeThisIndex = 0
for number in numbers[preambleLen:]:
    if not isValid(numbers, number):
        print("First non matching: " + str(number))
        invalidNumber = number
        break
    preamble[changeThisIndex] = number
    changeThisIndex = (changeThisIndex + 1) % preambleLen

#Part 2
totalSumList = findEncyptionWeakness(numbers, 0, invalidNumber)
print("Encryption weakness: " + str(min(totalSumList) + max(totalSumList)))