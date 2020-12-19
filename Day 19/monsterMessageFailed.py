# .... RIP recursion with Python
def getAllPossibilities(rule, rules, currentPossibilities):
    if ' | ' in rule:
        orRules = rule.split(' | ')
        newPossibilities = currentPossibilities.copy()
        newPossibilities2 = currentPossibilities.copy()
        currentPossibilities = getAllPossibilities(orRules[0], rules, newPossibilities)
        newerPossibilities = getAllPossibilities(orRules[1], rules, newPossibilities2)
        for possibility in newerPossibilities:
            currentPossibilities.append(possibility)
    else:
        for char in rule:
            if char == 'a' or char == 'b':
                for i in range(len(currentPossibilities)):
                    currentPossibilities[i] += char
            elif char.isnumeric():
                currentPossibilities = getAllPossibilities(rules[char], rules, currentPossibilities)
    return currentPossibilities

input = open("input.txt")

rules = {}
messages = []
readingRules = True
for line in input:
    stripped = line.strip()
    if not stripped:
        readingRules = False
    else:
        if readingRules:
            ruleNumberAndRules = stripped.split(': ')
            ruleNumber = ruleNumberAndRules[0]
            rules[ruleNumber] = ruleNumberAndRules[1]
        else:
            messages.append(stripped)
input.close()

allPossibilitiesFor0 = getAllPossibilities(rules['0'], rules, [""])

print(allPossibilitiesFor0)
matching = 0
for message in messages:
    print("checking " + message)
    if message in allPossibilitiesFor0:
        matching += 1

print(str(matching) + " completely match rules 0.")
