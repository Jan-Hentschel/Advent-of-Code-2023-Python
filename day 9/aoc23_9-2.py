product = 0
lines = []
with open(".\day 9\input.txt", "r") as input:
    lines = input.readlines()

def nextDimension(lastDimension):
    dimensions.append(lastDimension[0])
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
    print(dimensions)
    for i in range(len(dimensions)-1):
        nextNum = (nextNum*-1) + dimensions[i+1]
    print(nextNum)
    product += nextNum
print(product)