import re
array2d = []
symbolList = []
numberList = []
with open(".\day 3\input.txt", "r") as input:
    lines = input.readlines()
    for lineIndex,line in enumerate(lines):
        array2d.append(line)

        symbolIterObject = re.finditer("[*|#|+|$]", line)
        
        for x in symbolIterObject:
            symbolList.append([lineIndex,x.start(), x.group()])

        numberIterObject = re.finditer("\d+", line)
        
        for x in numberIterObject:
            numberList.append([lineIndex,(x.start(), x.end()-1), x.group()])

        
#print(array2d[1][38])
#print(symbolList)
#print(numberList)