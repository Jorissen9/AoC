numbers = []
input = open("input.txt")

for line in input:
    numbers.append(int(line))

found = False
for number in numbers:
    for number2 in numbers:
        if (number + number2 == 2020):
            print("result: " + str(number * number2))
            found = True
            break
    if found: 
        break

for number in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if (number + number2 + number3 == 2020):
                print("result: " + str(number * number2 * number3))
                exit()
