timeAndBusses = []
input = open("input.txt")

for line in input:
    timeAndBusses.append(line.strip())

myTime = int(timeAndBusses[0])
busses = timeAndBusses[1].split(',')

shortestTimeToWait = 9999999999999999
busNummerToWaitFor = "Not Found"
for bus in busses:
    if bus == 'x':
        next
    else:
        busNummer = int(bus)
        timeSinceLastBus = myTime % busNummer
        timeToWait = busNummer - timeSinceLastBus
        if timeToWait < shortestTimeToWait:
            shortestTimeToWait = timeToWait
            busNummerToWaitFor = busNummer

print("Id times bus# for some reason: " + str(shortestTimeToWait * busNummerToWaitFor))

#Part 2
highestBusNr = 0
bussNumbers = []
for bus in busses:
    if bus == 'x':
        next
    else:
        bussNumbers.append((busses.index(bus), int(bus)))
        if int(bus) > highestBusNr:
            highestBusNr = int(bus)
highestBusNrIndex = busses.index(str(highestBusNr))

liveData = True
if liveData:
    diff = 100000000000000 % int(highestBusNr)
    timeStamp = 100000000000000 + (int(highestBusNr) - diff)
else:
    timeStamp = int(highestBusNr)

step = 1
while bussNumbers: 
    for index, bus in bussNumbers: 
        if (timeStamp + index) % bus == 0: 
            bussNumbers.remove((index, bus)) 
            step *= bus 
        else: 
            timeStamp += step 
            break

print("Found timestamp: " + str(timeStamp))
