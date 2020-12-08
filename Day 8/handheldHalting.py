bootCode = []
input = open("input.txt")

for line in input:
    bootCode.append(line.strip())

accumulator = 0
i = 0
iAlreadyDone = []
while i < len(bootCode):
    if i in iAlreadyDone:
        break
    iAlreadyDone.append(i)

    currentLine = bootCode[i]
    operation = currentLine[:3]
    argument = int(currentLine[3:])

    if operation == "acc":
        accumulator += argument
    elif operation == "jmp":
        i += argument - 1
    # elif operation == "nop":
        # Nope
    i += 1
        
print("Accumulator after first duplicate instruction: " + str(accumulator))

#Part 2
def checkBootCode(bootCode, swapNumber):
    j = 0
    accumulator = 0
    jAlreadyDone = []
    ignoredCount = 0
    while j < len(bootCode):
        if j in jAlreadyDone:
            return False
        jAlreadyDone.append(j)

        currentLine = bootCode[j]
        operation = currentLine[:3]
        argument = int(currentLine[3:])

        if operation == "acc":
            accumulator += argument
        elif operation == "jmp":
            if ignoredCount != swapNumber:
                j += argument - 1
            ignoredCount += 1
        elif operation == "nop":
            if ignoredCount == swapNumber:
                j += argument - 1
            ignoredCount += 1
        j += 1
    return accumulator

# Brute force them change!
fixedProgramAcc = "Not Found"
count = 0
while fixedProgramAcc == "Not Found" and count < len(bootCode):
    checked = checkBootCode(bootCode, count)
    if not checked:
        count += 1
    else:
        fixedProgramAcc = checked
        break

print("Accumulator after full completion: " + str(fixedProgramAcc))