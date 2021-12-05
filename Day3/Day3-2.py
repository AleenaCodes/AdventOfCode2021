import math

digitsInNumber = 12

report = []

with open('input.txt', 'r') as numbers:
    for number in numbers:
        report.append(list(number))

# return the most or list common value at a specific index
def getDigitToFilterOn(valuesList, index, most):
    sum = 0
    # if the sum is >= this then 1 is the most common number
    halfLengthOfNumbers = math.ceil(len(valuesList) / 2)

    for x in range (0, len(valuesList)):
        sum += int(valuesList[x][index])

    if (most == True):
        if(sum >= halfLengthOfNumbers):
            return '1'
        else:
            return '0'
    else:
        if(sum < halfLengthOfNumbers):
            return '1'
        else:
            return '0'

# filter list for specific digit at specific index
def filterListAtIndex(valuesList, index, digit):
    listCopy = list(valuesList)
    filteredList = list(filter(lambda value: value[index] == digit, listCopy))
    return filteredList

# find the oxygen rating

oxygenfiltered = list(report)
index = 0

while((len(oxygenfiltered) > 1) & (index < digitsInNumber)):
    digitToFilterOn = getDigitToFilterOn(oxygenfiltered, index, True)
    oxygenfiltered = filterListAtIndex(oxygenfiltered, index, digitToFilterOn)
    index += 1

# find the co2 rating

co2filtered = list(report)
index = 0

while((len(co2filtered) > 1) & (index < digitsInNumber)):
    digitToFilterOn = getDigitToFilterOn(co2filtered, index, False)
    co2filtered = filterListAtIndex(co2filtered, index, digitToFilterOn)
    index += 1

# turn into ints and multiply

oxygenString = "".join(oxygenfiltered[0])
co2String = "".join(co2filtered[0])

oxygen = int(oxygenString, 2)
co2 = int(co2String, 2)

print(oxygenfiltered[0], " ", co2filtered[0])
print(oxygen, " ", co2)
print("total ", oxygen * co2)