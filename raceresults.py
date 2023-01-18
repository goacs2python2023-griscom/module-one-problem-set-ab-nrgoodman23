#Modified to work with any number of other racers.
#Inputs are your time first, and then an array containing every other time in any order.
def medal(yourTime, otherTimes):
    gold = yourTime
    silver = yourTime
    bronze = yourTime

    for time in otherTimes:
        if gold != None and time < gold:
            gold = None
        elif silver != None and time < silver:
            silver = None
        elif bronze != None and time < bronze:
            bronze = None
    
    if gold != None:
        return "Gold"
    elif silver != None:
        return "Silver"
    elif bronze != None:
        return "Bronze"
    else:
        return "No Medal"