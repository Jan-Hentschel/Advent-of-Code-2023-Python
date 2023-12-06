import re
sum = 0
array2d = []
symbolList = []
numberList = []
with open(".\day 3\input.txt", "r") as input:
    lines = input.readlines()
    for lineIndex,line in enumerate(lines):
        array2d.append(line)

        symbolIterObject = re.finditer("[*]", line)
        
        for x in symbolIterObject:
            symbolList.append([lineIndex,x.start()])

        numberIterObject = re.finditer("\d+", line)
        
        for x in numberIterObject:
            numberList.append([lineIndex,(x.start(), x.end()-1), x.group()])

        

for symbol in symbolList:
    lineIndex = symbol[0]
    indexInLine = symbol[1]
    numberObjects = []
    #all numbers in adjacent and same line
    for numberObject in numberList:
        if numberObject[0] == lineIndex-1 or numberObject[0] == lineIndex or numberObject[0] == lineIndex+1:
            
            if indexInLine in range(numberObject[1][0]-1, numberObject[1][1]+2):
                numberObjects.append(numberObject)
    if len(numberObjects) == 2:
        sum += int(numberObjects[0][2])*int(numberObjects[1][2])
    

print(sum)