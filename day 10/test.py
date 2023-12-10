lines = []
with open(".\day 10\inptuttest.txt", "r") as input:
    lines = input.readlines()
lines = [line.replace("\n", "") for line in lines]

numTiles = 0

pipes = {
    "|": ("north", "south"),
    "-": ("east", "west"),
    "L": ("north", "east"),
    "J": ("north", "west"),
    "7": ("south", "west"),
    "F": ("south", "east")
}

newMapDict = {
    (22,91): ["west", "S", 0]
              
}

currentPosition = (22, 90)
steps = 1
lastDirection = "east"

while currentPosition != (22, 91):
    currentChar = lines[currentPosition[0]][currentPosition[1]]
    nextDirection = ""
    if pipes[currentChar][0] == lastDirection:
        nextDirection = pipes[currentChar][1]
    elif pipes[currentChar][1] == lastDirection:
        nextDirection = pipes[currentChar][0]
        
    newMapDict[currentPosition] = [nextDirection, currentChar, steps]

    if nextDirection == "south":
        currentPosition = (currentPosition[0] + 1, currentPosition[1])
        lastDirection = "north"
    elif nextDirection == "west":
        currentPosition = (currentPosition[0], currentPosition[1] - 1)
        lastDirection = "east"
    elif nextDirection == "north":
        currentPosition = (currentPosition[0] - 1, currentPosition[1])
        lastDirection = "south"
    elif nextDirection == "east":
        currentPosition = (currentPosition[0], currentPosition[1] + 1)
        lastDirection = "west"
    steps += 1

for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if not((y,x) in newMapDict):
            isOutside = 0
            position = [y,x]
            while position[1]>=0:
                if tuple(position) in newMapDict:
                    pipeDir = newMapDict[tuple(position)][0]
                    if pipeDir == "north":
                        isOutside -= 1
                    elif pipeDir == "south":
                        isOutside += 1
                position[1]-=1
            print(isOutside)
            if isOutside != 0:
                numTiles += 1



print(numTiles)