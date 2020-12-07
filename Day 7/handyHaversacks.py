def findAndCount(searchedColor, parentsAndTheirChildren, possibleColors):
    for parent, children in parentsAndTheirChildren.items():
        for child in children:
            if searchedColor == child["color"]:
                if parent not in possibleColors:
                    possibleColors.append(parent)
                possibleColors = findAndCount(parent, parentsAndTheirChildren, possibleColors)

    return possibleColors

def findAndCountAmount(searchedColor, parentsAndTheirChildren):
    amountOfBags = 0
    for child in parentsAndTheirChildren[searchedColor]:
        amountOfBags += child["amount"] + child["amount"] * findAndCountAmount(child["color"], parentsAndTheirChildren)

    return amountOfBags

input = open("input.txt")

parentsAndTheirChildren = {}
for line in input:
    strippedLine = line.strip()
    parentAndChildren = strippedLine.split('bags contain')
    parentBag = parentAndChildren[0].strip()
    parentsAndTheirChildren[parentBag] = []

    if parentAndChildren[1] != " no other bags.":
        children = parentAndChildren[1].strip().split(',')
        for child in children:
            childBag = {}
            childBag["amount"] = int(child.strip()[0])
            childBag["color"] = child.strip().rstrip('.')[1:-4].strip() # bags or _bag :)
            parentsAndTheirChildren[parentBag].append(childBag)

print("Bags containing shiny gold: ", len(findAndCount("shiny gold", parentsAndTheirChildren, [])))
print("Amount of bags in my shiny gold bag: ", findAndCountAmount("shiny gold", parentsAndTheirChildren))
