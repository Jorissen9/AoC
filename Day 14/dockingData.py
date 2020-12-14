def applyMask(currentMask, binValueStr):
    maskLen = len(currentMask)
    valueAfterMask = 0
    for i in range(maskLen):
        maskChar = currentMask[maskLen - 1 - i]

        if i < len(binValueStr):
            binChar = binValueStr[len(binValueStr) - 1 - i]
            if maskChar == '1' or (maskChar == 'X' and binChar == '1'):
                valueAfterMask += 2**i
        else:
            if maskChar == '1':
                valueAfterMask += 2**i

    return valueAfterMask

def applyMaskV2(currentMask, memValueStr):
    maskLen = len(currentMask)
    valueStrAfterMask = ""
    for i in range(maskLen):
        maskChar = currentMask[i]

        if maskLen - i <= len(memValueStr):
            memChar = memValueStr[i - maskLen]
            if maskChar == '1':
                valueStrAfterMask = valueStrAfterMask + maskChar
            if maskChar == 'X':
                valueStrAfterMask = valueStrAfterMask + maskChar
            if maskChar == '0':
                valueStrAfterMask = valueStrAfterMask + memChar
        else:
            valueStrAfterMask = valueStrAfterMask + maskChar

    return valueStrAfterMask

def getMemoryAdressesFromMask(memMask, currentMaskPart, memoryAdresses, indexesTodo):
    createdMask = currentMaskPart
    while len(createdMask) < len(memMask):
        char = memMask[len(createdMask)]
        if char == 'X':
            if len(createdMask) + 1 in indexesTodo:
                createdMask = createdMask + '1'
                indexesTodo.remove(len(createdMask))
            else:
                createdMask = createdMask + '0'
                indexesTodo.append(len(createdMask))
        else:
            createdMask += char

    memoryAdresses.append(createdMask)
    if not indexesTodo:
        return memoryAdresses
    else:
        lastIndexTodo = indexesTodo[-1]
        newMask = createdMask[:lastIndexTodo - 1]
        return getMemoryAdressesFromMask(memMask, newMask, memoryAdresses, indexesTodo)

dockingCode = []
input = open("input.txt")

for line in input:
    dockingCode.append(line.strip())

memory = {}
memoryV2 = {}
currentMask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
maskValue = 0
for codeLine in dockingCode:
    if codeLine[:4] == "mask":
        currentMask = codeLine[7:]
    else:
        memAndValue = codeLine.split('=')
        mem = memAndValue[0][4:-2]
        value = int(memAndValue[1])
        binValueStr = str(bin(value))[2:]

        #Part 1
        valueAfterMask = applyMask(currentMask, binValueStr)
        memory[mem] = valueAfterMask

        #Part 2
        memStr = str(bin(int(mem)))[2:]
        memMask = applyMaskV2(currentMask, memStr)
        memAdresses = getMemoryAdressesFromMask(memMask, '', [], [])
        for memAdress in memAdresses:
            memoryV2[int(memAdress, 2)] = value

totalSum = 0
for value in memory.values():
    totalSum += value

print("Sum of all values in memory: " + str(totalSum))

totalSum = 0
for value in memoryV2.values():
    totalSum += value
print("Sum of all values in memory V2: " + str(totalSum))
