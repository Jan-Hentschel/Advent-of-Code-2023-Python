lines = []
with open(".\day 8\input.txt", "r") as input:
    lines = input.readlines()

dict = {}
for line in lines[2:]:
    dict[line[:3]] = (line[7:10], line[12:15])

instructions = lines[0].replace("\n", "")
print(instructions)
steps = 0

def allKeysEndInZ(currentKeys):
    for key in currentKeys:
        if key[2] != "Z":
            return True
    return False


currentKeys = []
for key in dict.keys():
    if key[2] == "A":
        currentKeys.append(key)
print(currentKeys)

while allKeysEndInZ(currentKeys):
    for char in instructions:
        for i,currentKey in enumerate(currentKeys):
            if char == "L":
                print(currentKey, dict[currentKey][0], steps, char)
                currentKeys[i] = dict[currentKey][0]
                
            elif char == "R":
                print(currentKey,dict[currentKey][1], steps, char)
                currentKeys[i] = dict[currentKey][1]
        print(currentKeys)
        steps +=1
print(steps)