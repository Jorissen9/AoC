policyLetterList = []
policyAmountList = []
passwordList = []
input = open("input.txt")

for line in input:
    policyAndPwd = line.split(':')
    policyLetterList.append(policyAndPwd[0].strip()[-1])
    policyAmountList.append(policyAndPwd[0][:-1].strip())
    passwordList.append(policyAndPwd[1].strip())

amountCorrectCounter = 0
positionCorrectCounter = 0
for i in range(len(passwordList)):
    policyLetter = policyLetterList[i]
    policyAmounts = policyAmountList[i].split("-")
    pwd = passwordList[i]

    minAmount = int(policyAmounts[0])
    maxAmount = int(policyAmounts[1])

    # part 1
    amountInPwd = int(pwd.count(policyLetter))
    if minAmount <= amountInPwd <= maxAmount:
        amountCorrectCounter += 1

    # part 2
    minAmountCorrect = pwd[minAmount-1] == policyLetter
    maxAmountCorrect = pwd[maxAmount-1] == policyLetter
    if not(pwd[minAmount-1] == policyLetter == pwd[maxAmount-1]) and (pwd[minAmount-1] == policyLetter or pwd[maxAmount-1] == policyLetter):
        positionCorrectCounter += 1
    
print("Amount correct:" + str(amountCorrectCounter))
print("position correct:" + str(positionCorrectCounter))
