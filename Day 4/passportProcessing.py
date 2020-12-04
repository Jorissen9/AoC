def validatePassport(passport):
    for key, value in passport.items():
        if key == "byr" and not(1920 <= int(value) <= 2002):
            return False
        elif key == "iyr" and not(2010 <= int(value) <= 2020):
            return False
        elif key == "eyr" and not(2020 <= int(value) <= 2030):
            return False
        elif key == "hgt":
            if not(value[-2:] == "cm" or value[-2:] == "in"):
                return False
            height = int(value[:-2])
            metric = value[-2:] == "cm"
            if (metric and not(150 <= height <= 193)) or (not metric and not(59 <= height <= 79)):
                return False
        elif key == "hcl" and not(value[0] == '#' and len(value) == 7 and all(valueChar.isnumeric() or ord('a') <= ord(valueChar) <= ord('f') for valueChar in value[1:])):
            return False
        elif key == "ecl" and value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        elif key == "pid" and not(len(value) == 9):
            return False

    return True

passportList = []
input = open("input.txt")

requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passportFields = {}
for line in input:
    strippedLine = line.strip()
    if not strippedLine:
        passportList.append(passportFields)
        passportFields = {}
    else:
        pairs = strippedLine.split(' ')
        for pair in pairs:
            keyAndValue = pair.split(':')
            passportFields[keyAndValue[0]] = keyAndValue[1]
passportList.append(passportFields)

presentPassports = 0
presentAndValidatedPassports = 0
for passport in passportList:
    if len(passport.keys()) >= len(requirements): 
        presentFields = 0
        for requirement in requirements:
            if requirement in passport.keys():
                presentFields += 1
        
        if presentFields == len(requirements):
            presentPassports += 1
            if (validatePassport(passport)):
                presentAndValidatedPassports += 1

print("Present passports: " + str(presentPassports))
print("Valid passports: " + str(presentAndValidatedPassports))
