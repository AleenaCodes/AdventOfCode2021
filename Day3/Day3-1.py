import math

digitsInNumber = 12

report = []

with open('input.txt', 'r') as numbers:
    for number in numbers:
        report.append(list(number))

# if the sum is >= this then 1 is the most common number
halfLengthOfNumbers = math.ceil(len(report) / 2)

sums = []

for x in range(0, digitsInNumber):
    sums.append(0)

for x in range (0, len(report)):
    for y in range(0, digitsInNumber):
        sums[y] += int(report[x][y])

gammaValues = []

for x in range (0, digitsInNumber):
    if (sums[x] >= halfLengthOfNumbers):
        gammaValues.append(1)
    else:
        gammaValues.append(0)

epsilonValues = []

for x in range(0, digitsInNumber):
    if (gammaValues[x] == 1):
        epsilonValues.append(0)
    else:
        epsilonValues.append(1)

gammaAsChars = list(map(lambda x: str(x), gammaValues))
epsilonAsChars = list(map(lambda x: str(x), epsilonValues))

gammaString = "".join(gammaAsChars)
epsilonString = "".join(epsilonAsChars)

gamma = int(gammaString, 2)
epsilon = int(epsilonString, 2)

print(gamma)
print(epsilon)