op = "operations"
num = "numbers"

def calculateInsideParenthesis(orderIndex, ordersToCalc):
    orderToCalc = ordersToCalc[orderIndex]
    numbers = orderToCalc[num]
    operations = orderToCalc[op]
    
    firstNumber = numbers[0]
    if isinstance(firstNumber, int):
        result = firstNumber
    else:
        result = calculateInsideParenthesis(int(firstNumber[1:]), ordersToCalc)

    for i in range(len(operations)):
        if isinstance(numbers[i + 1], int):
            numberToCalcWith = numbers[i + 1]
        else:
            numberToCalcWith = calculateInsideParenthesis(int(numbers[i + 1][1:]), ordersToCalc)

        if operations[i] == '+':
            result += numberToCalcWith
        elif operations[i] == '*':
            result *= numberToCalcWith

    return result

def calculateInsideParenthesisWhileBeingWeird(orderIndex, ordersToCalc):
    orderToCalc = ordersToCalc[orderIndex]
    numbers = orderToCalc[num]
    operations = orderToCalc[op]
    
    if not isinstance(numbers[0], int):
        numbers[0] = calculateInsideParenthesisWhileBeingWeird(int(numbers[0][1:]), ordersToCalc)

    for i in range(len(operations)):
        if operations[i] == '+':
            if isinstance(numbers[i + 1], int):
                numberToCalcWith = numbers[i + 1]
            elif numbers[i + 1][:1] == '(':
                numberToCalcWith = calculateInsideParenthesisWhileBeingWeird(int(numbers[i + 1][1:]), ordersToCalc)
            numbers[i + 1] = False

            index = i
            while not numbers[index]:
                index -= 1
            if not isinstance(numbers[index], int) and numbers[index][:1] == '(':
                numbers[index] = calculateInsideParenthesisWhileBeingWeird(int(numbers[i][1:]), ordersToCalc)
            numbers[index] += numberToCalcWith
    
    for i in range(len(operations)):
        if operations[i] == '*':
            if isinstance(numbers[i + 1], int):
                numberToCalcWith = numbers[i + 1]
            elif numbers[i + 1][:1] == '(':
                numberToCalcWith = calculateInsideParenthesisWhileBeingWeird(int(numbers[i + 1][1:]), ordersToCalc)
            numbers[i + 1] = False
            
            index = i
            while not numbers[index]:
                index -= 1
            numbers[index] *= numberToCalcWith

    return numbers[0]
    
input = open("input.txt")

expressions = []
for line in input:
    expressions.append(line.strip())
input.close()

expressionResults = []
expressionResultsPart2 = []
for expression in expressions:
    ordersToCalc = []
    closedNumbers = []
    numberToCalc = 0
    
    ordersToCalc.append({})
    ordersToCalc[numberToCalc][op] = []
    ordersToCalc[numberToCalc][num] = []
    for char in expression:
        if char.isnumeric():
            ordersToCalc[numberToCalc][num].append(int(char))
        elif char == '+' or char == '*':
            ordersToCalc[numberToCalc][op].append(char)
        elif char == '(':
            nextNumberToCalc = len(ordersToCalc)
            ordersToCalc[numberToCalc][num].append(char + str(nextNumberToCalc))
            numberToCalc = nextNumberToCalc
            ordersToCalc.append({})
            ordersToCalc[numberToCalc][op] = []
            ordersToCalc[numberToCalc][num] = []
        elif char == ')':
            closedNumbers.append(numberToCalc)
            while numberToCalc in closedNumbers:
                numberToCalc -= 1
    
    expressionResult = calculateInsideParenthesis(0, ordersToCalc)
    expressionResults.append(expressionResult)

    expressionResultPart2 = calculateInsideParenthesisWhileBeingWeird(0, ordersToCalc)
    expressionResultsPart2.append(expressionResultPart2)

totalSum = 0
for result in expressionResults:
    totalSum += result
print("Total sum: " + str(totalSum))

totalSum = 0
for result in expressionResultsPart2:
    totalSum += result
print("Total sum part 2: " + str(totalSum))
