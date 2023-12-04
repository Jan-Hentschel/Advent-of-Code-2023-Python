digits = ["1","2","3","4","5","6","7","8","9"]
with open('.\day 1\input.txt', "r") as input:
    sum = 0
    lines = input.readlines()
    for line in lines:
        firstDigit = ""
        lastDigit = ""
        first = True
        for char in line:
            if char in digits:
                if first == True:
                    firstDigit = char
                    first = False
                lastDigit = char
        sum+=int(firstDigit+lastDigit)
    print(sum)