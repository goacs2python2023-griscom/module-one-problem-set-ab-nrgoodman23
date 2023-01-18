#I made it work for any side count of dice
def chance(goalNums, diceSides):
    a, b = map(int, goalNums.split(" "))
    diceSides = diceSides.split(" ")

    aTotal = 0
    bTotal = 0

    for side in diceSides:
        if a == int(side):
            aTotal += 1
        if b == int(side):
            bTotal += 1
    
    return (aTotal / len(diceSides)) * (bTotal / len(diceSides))