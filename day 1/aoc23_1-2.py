import re

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


with open(".\day 1\input.txt") as f:
    sum = 0
    lines = f.readlines()
    firstDigit = ""
    lastDigit = ""
    for line in lines:
        foundDigits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
        if foundDigits[0] in digits:
            firstDigit = str(digits.index(foundDigits[0])+1)
        else:
            firstDigit = foundDigits[0]

        if foundDigits[-1] in digits:
            lastDigit = str(digits.index(foundDigits[-1])+1)
        else:
            lastDigit = foundDigits[-1]
        sum = sum + int(firstDigit + lastDigit)

    print(sum)