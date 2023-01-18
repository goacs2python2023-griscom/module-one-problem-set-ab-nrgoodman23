def busesNeeded(people):
    if people % 52 == 0:
        return people / 52
    else:
        return (people / 52) - ((people % 52) / 52) + 1