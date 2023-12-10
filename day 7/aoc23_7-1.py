lines = []
with open(".\day 7\input.txt", "r") as input:
    lines = input.readlines()

def determineType(line):
    elements = line.split()
    cards = elements[0]
    
    card_count = {}  # Dictionary to store character counts

    # Count occurrences of each character in the string
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    # Find the most common character and its count
    most_common_card = max(card_count, key=card_count.get)
    count_of_most_common_card = card_count[most_common_card]
    if count_of_most_common_card == 5:
        return "five"
    if count_of_most_common_card == 4:
        return "four"
    if count_of_most_common_card == 3 and len(card_count) == 2:
        return "full"
    if count_of_most_common_card == 3:
        return "three"
    if count_of_most_common_card == 2 and len(card_count) == 3:
        return "two"
    if count_of_most_common_card == 2:
        return "one"
    if count_of_most_common_card == 1:
        return "high"

typeList = ["five", "four", "full", "three", "two", "one", "high"]
cardList = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def card1Better(line1, line2):
    for i in range(5):
        if cardList.index(line1[i]) < cardList.index(line2[i]):
            return True
        elif cardList.index(line1[i]) > cardList.index(line2[i]):
            return False

def shouldSwap(line1, line2):
    type1 = determineType(line1)
    type2 = determineType(line2)
    if typeList.index(type1) > typeList.index(type2):
        return True
    elif typeList.index(type1) < typeList.index(type2):
        return False
    elif typeList.index(type1) == typeList.index(type2):
        if card1Better(line1, line2):
            return False
        elif not(card1Better(line1, line2)):
            return True

def bubbleSort(lines):
    n = len(lines)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if shouldSwap(lines[j], lines[j + 1]):
                swapped = True
                lines[j], lines[j + 1] = lines[j + 1], lines[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
bubbleSort(lines)

lines = [line.replace("\n","") for line in lines]
lines.reverse()
sum = 0
for i,line in enumerate(lines):
    print(line, i+1, (i+1)*int(line[5:].strip()))
    sum+=(i+1)*int(line[5:].strip())

print(sum)