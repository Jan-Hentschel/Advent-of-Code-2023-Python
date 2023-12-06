with open(".\day 6\input.txt", "r") as input:
    lines = input.readlines()
    raceTime = lines[0][11:].replace(" ", "")
    raceDistance = lines[1][11:].replace(" ", "")

    buttonTime = 0
    distance = 0
    ways = 0
    for o in range(1,int(raceTime)):
        time = int(raceTime)
        buttonTime = o
        timeLeft = time - buttonTime
        distance = timeLeft*buttonTime
        if distance > int(raceDistance):
            ways += 1
    print(ways)