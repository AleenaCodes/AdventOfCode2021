depth = 0
horizontal = 0
aim = 0

with open('input-1.txt', 'r') as instructions:
    for instruction in instructions:

        direction = instruction.split()[0]
        value = int(instruction.split()[1])

        if (direction == "forward"):
            horizontal += value
            depth += value*aim
        elif (direction == "down"):
            aim += value
        elif (direction == "up"):
            aim -= value
        else:
            print("gone wrong")

print(depth)
print(horizontal)