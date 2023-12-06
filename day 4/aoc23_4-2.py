scratchcardAmount=0
with open(".\day 4\input.txt", "r") as input:
    scratchcards=input.readlines()
    for i,scratchcard in enumerate(scratchcards):
        matches = 0
        winningNumbers = scratchcard[10:40].split()
        currentNumbers = scratchcard[41:116].split()
        for currentNumber in currentNumbers:
            if currentNumber in winningNumbers:
                matches += 1
        for o in range(1,matches+1):
            scratchcards.append(scratchcards[o])
        print(matches)
