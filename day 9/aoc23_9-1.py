product = 0
lines = []
with open(".\day 9\input.txt", "r") as input:
    lines = input.readlines()

def nextDimension(lastDimension):
    dimensions.append(lastDimension[len(lastDimension)-1])
    if sum(lastDimension) == 0:
        return
    nextNumbers = []
    for i in range(len(lastDimension)-1):
        nextNumbers.append(int(lastDimension[i+1])-int(lastDimension[i]))
    nextDimension(nextNumbers)

for line in lines:
    nextNum = 0
    numbers = line.split()
    numbers = [int(element) for element in numbers]
    dimensions = []
    nextDimension(numbers)
    dimensions = dimensions[::-1]
    
    for i in range(len(dimensions)-1):
        nextNum += dimensions[i+1]

    product += nextNum
print(product)