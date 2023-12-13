games = []
with open("AoCday2Data", 'r') as source:
    games = source.readlines()

maxred = 12
maxgreen = 13
maxblue = 14
count = 1
wins = []
powers = []
for game in games:
    red = []
    blue = []
    green = []
    rounds = game.split(';')
    print(rounds)
    for round in rounds:
        if "red" in round:
            rednum = ''
            redindex = round.index("red")
            temp = round[redindex-3:redindex]
            for each in temp:
                if each.isdigit():
                    rednum += each
            red.append(int(rednum))
        if "blue" in round:
            bluenum = ''
            blueindex = round.index("blue")
            temp = round[blueindex-3:blueindex]
            for each in temp:
                if each.isdigit():
                    bluenum += each
            blue.append(int(bluenum))
        if "green" in round:
            greennum = ''
            greenindex = round.index("green")
            temp = round[greenindex-3:greenindex]
            for each in temp:
                if each.isdigit():
                    greennum += each
            green.append(int(greennum))
    if max(red) <= maxred and max(green) <= maxgreen and max(blue) <= maxblue:
        wins.append(count)
    powers.append((max(blue) * max(green) * max(red)))
    count += 1
print(sum(wins))
print(sum(powers))