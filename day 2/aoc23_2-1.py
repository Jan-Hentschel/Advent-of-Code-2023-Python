with open(".\day 2\input.txt", "r") as input:
    sum=0
    lines = input.readlines()
    ID=1
    for line in lines:
        redMax = 0
        greenMax = 0
        blueMax = 0
        if ID < 9:
            games = line[8:].split(";")
        elif ID < 100:
            games = line[9:].split(";")
        else:
            games = line[10:].split(";")
        
        for throw in games:
            throw = throw.replace("\n", "")
            throw = throw.replace(" ", "")
            picks = throw.split(",")
            for pick in picks:
                if pick[-3:] == "red":
                    if len(pick) - 3 == 2:
                        if redMax < int(pick[0]+pick[1]):
                            redMax = int(pick[0]+pick[1])
                    else:
                        if redMax < int(pick[0]):
                            redMax = int(pick[0])
                if pick[-5:] == "green":
                    if len(pick) - 5 == 2:
                        if greenMax < int(pick[0]+pick[1]):
                            greenMax = int(pick[0]+pick[1])
                    else:
                        if greenMax < int(pick[0]):
                            greenMax = int(pick[0])
                if pick[-4:] == "blue":
                    if len(pick) - 4 == 2:
                        if blueMax < int(pick[0]+pick[1]):
                            blueMax = int(pick[0]+pick[1])
                    else:
                        if blueMax < int(pick[0]):
                            blueMax = int(pick[0])

        if redMax <= 12 and greenMax <= 13 and blueMax <= 14:
            sum += ID
            print(sum)
        ID+=1
        