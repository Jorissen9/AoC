def determine(maxNumber, numbers):
    numbersSpoken = {}
    prevNumbersSpoken = {}

    for number in numbers:
        numbersSpoken[int(number)] = numbers.index(number) + 1
    numberSpoken = numbers[-1]

    for i in range(len(numbers), maxNumber):
        if numberSpoken in prevNumbersSpoken.keys():
            numberSpoken = i - prevNumbersSpoken[numberSpoken]
        else:
            numberSpoken = 0

        if numberSpoken in numbersSpoken.keys():
            prevNumbersSpoken[numberSpoken] = numbersSpoken[numberSpoken]
        numbersSpoken[numberSpoken] = i + 1

numbers = []
input = open("input.txt")

for line in input:
    for char in line.strip().split(','):
        numbers.append(int(char))

determine(2020, numbers)
determine(30000000, numbers)
