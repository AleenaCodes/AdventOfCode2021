inputFile = open("input-1.txt", 'r')
answer = 0

# Get first measurement
prevDepthMeasurement = int(inputFile.readline())

# Keep comparing to prev and increment answer
while prevDepthMeasurement:
    newDepthMeasurement = inputFile.readline()
    if (newDepthMeasurement) == "":
        break
    else:
        newDepthMeasurement = int(newDepthMeasurement)

    if ((newDepthMeasurement - prevDepthMeasurement) > 0):
        answer += 1

    prevDepthMeasurement = newDepthMeasurement

inputFile.close()

print(answer)