def checkRule(rules, rule, message):
    if not rule:
        yield message
    else:
        ruleIndex, *rule = rule
        for message in checkRules(rules, ruleIndex, message):
            yield from checkRule(rules, rule, message)

def checkOrStuff(rules, orStuff, message):
    for rule in orStuff:
        yield from checkRule(rules, rule, message)

def checkRules(rules, ruleIndex, message):
    if isinstance(rules[ruleIndex], list):
        yield from checkOrStuff(rules, rules[ruleIndex], message)
    else:
        if message and message[0] == rules[ruleIndex]:
            yield message[1:]

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
            ruleNumber, rule = stripped.split(': ')
            if rule[0] == '"':
                rule = rule[1:-1]
            else:
                rule = [part.split(' ') if ' ' in part else [part]
                        for part in (rule.split(' | ') if ' | ' in rule else [rule])]
            rules[ruleNumber] = rule
        else:
            messages.append(stripped)
input.close()

totalMatch = 0
for message in messages:
    if any(m == '' for m in checkRules(rules, '0', message)):
        totalMatch += 1

print('Part 1 match: ' + str(totalMatch))

#Part 2
rules = {**rules, '8': [['42'], ['42', '8']], '11': [['42', '31'], ['42', '11', '31']]}

totalMatch = 0
for message in messages:
    if any(m == '' for m in checkRules(rules, '0', message)):
        totalMatch += 1
print('Part 2 match: ' + str(totalMatch))
