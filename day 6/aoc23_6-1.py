product = 1
with open(".\day 6\input.txt", "r") as input:
    lines = input.readlines()
    raceTimes = lines[0][11:].split()
    raceDistances = lines[1][11:].split()
    for i in range(4):
        buttonTime = 0
        distance = 0
        ways = 0
        for o in range(1,int(raceTimes[i])):
            time = int(raceTimes[i])
            buttonTime = o
            timeLeft = time - buttonTime
            distance = timeLeft*buttonTime
            if distance > int(raceDistances[i]):
                ways += 1
        product*=ways
print(product)