sum=0
with open(".\day 4\input.txt", "r") as input:
    scratchcards=input.readlines()
    for scratchcard in scratchcards:
        matches = 0
        winningNumbers = scratchcard[10:40].split()
        currentNumbers = scratchcard[41:116].split()
        for currentNumber in currentNumbers:
            if currentNumber in winningNumbers:
                matches += 1
        if matches > 0:
            sum += 2**(matches-1)
print(sum)