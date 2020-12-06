input = open("input.txt")

uniqueChars = []
sumOfCounts = 0

allChars = ''
sumOfEveryone = 0
for line in input:
    strippedLine = line.strip()
    if strippedLine == '':
        sumOfCounts += len(uniqueChars)
        uniqueChars = []

        sumOfEveryone += len(allChars)
        allChars = ''
    else:
        #Part 2
        if uniqueChars == []:
            allChars = strippedLine
        else:
            for char in allChars:
                if char not in strippedLine:
                    allChars = allChars.replace(char, '')

        #Part 1
        for char in strippedLine:
            if char not in uniqueChars:
                uniqueChars.append(char)


sumOfCounts += len(uniqueChars)
sumOfEveryone += len(allChars)

print("Sum of counts: " + str(sumOfCounts))
print("Sum of everyone: " + str(sumOfEveryone))