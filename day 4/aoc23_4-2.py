scratchcardAmount=215

def getMatches(scratshcard):
    matches = 0
    winningNumbers = scratchcard[10:40].split()
    currentNumbers = scratchcard[41:116].split()
    for currentNumber in currentNumbers:
        if currentNumber in winningNumbers:
            matches += 1
    return matches

scratchesAndSolutions = []

with open(".\day 4\input.txt", "r") as input:
    scratchcards=input.readlines()
    for i,scratchcard in enumerate(scratchcards):
        scratchesAndSolutions.append([i,getMatches(scratchcard), 1])


for object in scratchesAndSolutions:
    print(object)
    while object[2] > 0:
        for i in range(object[1]):
            scratchesAndSolutions[i+object[0]+1][2]+=1
            scratchcardAmount+=1

        object[2]-=1
print(scratchcardAmount)