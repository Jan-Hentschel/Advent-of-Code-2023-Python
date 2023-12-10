lines = []
with open(".\day 10\input.txt", "r") as input:
    lines = input.readlines()
lines = [line.replace("\n", "") for line in lines]

pipes = {
    "|": ("north", "south"),
    "-": ("east", "west"),
    "L": ("north", "east"),
    "J": ("north", "west"),
    "7": ("south", "west"),
    "F": ("south", "east")
}

currentPosition = (22, 90)
steps = 1
lostDirection = "east"

while currentPosition != (22, 91):
    currentChar = lines[currentPosition[0]][currentPosition[1]]
    nextDirection = ""
    if pipes[currentChar][0] == lostDirection:
        nextDirection = pipes[currentChar][1]
    elif pipes[currentChar][1] == lostDirection:
        nextDirection = pipes[currentChar][0]

    if nextDirection == "south":
        currentPosition = (currentPosition[0] + 1, currentPosition[1])
        lostDirection = "north"
    elif nextDirection == "west":
        currentPosition = (currentPosition[0], currentPosition[1] - 1)
        lostDirection = "east"
    elif nextDirection == "north":
        currentPosition = (currentPosition[0] - 1, currentPosition[1])
        lostDirection = "south"
    elif nextDirection == "east":
        currentPosition = (currentPosition[0], currentPosition[1] + 1)
        lostDirection = "west"
    steps += 1

farthest = steps / 2
print(farthest)