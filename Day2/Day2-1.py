depth = 0
horizontal = 0

with open('input-1.txt', 'r') as instructions:
    for instruction in instructions:

        direction = instruction.split()[0]
        value = int(instruction.split()[1])

        if (direction == "forward"):
            horizontal += value
        elif (direction == "down"):
            depth += value
        elif (direction == "up"):
            depth -= value
        else:
            print("gone wrong")

print(depth)
print(horizontal)