inputFile = open("input-1.txt", 'r')

# Get values for first window
slidingWindow = [0,0,0]
slidingMeasurements = []

first = int(inputFile.readline())
slidingWindow[0] = first
second = int(inputFile.readline())
slidingWindow[1] = second
third = int(inputFile.readline())
slidingWindow[2] = third

# Calc first average value
slidingMeasurements.append((slidingWindow[0] + slidingWindow[1] + slidingWindow[2]) / 3)

# Keep sliding window and calculating new average values
while third:
    third = inputFile.readline()
    if (third) == "":
        break
    else:
        third = int(third)

    slidingWindow[0] = slidingWindow[1]
    slidingWindow[1] = slidingWindow[2]
    slidingWindow[2] = third

    slidingMeasurements.append((slidingWindow[0] + slidingWindow[1] + slidingWindow[2]) / 3)

inputFile.close()

# Run through compiled averages and compare to prev
answer = 0

for x in range (1, len(slidingMeasurements)):
    if (slidingMeasurements[x] - slidingMeasurements[x-1] > 0):
        answer += 1

print(answer)