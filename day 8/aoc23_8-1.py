lines = []
with open(".\day 8\input.txt", "r") as input:
    lines = input.readlines()

dict = {}
for line in lines[2:]:
    dict[line[:3]] = (line[7:10], line[12:15])

instructions = lines[0].replace("\n", "")
print(instructions)
steps = 0
currentKey = "AAA"
while currentKey != "ZZZ":
    for char in instructions:
        if char == "L":
            currentKey = dict[currentKey][0]
        elif char == "R":
            currentKey = dict[currentKey][1]
        steps +=1

print(steps)