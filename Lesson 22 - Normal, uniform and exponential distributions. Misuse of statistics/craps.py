from random import choice
from matplotlib import pyplot as plt


def rollDice():
    dice = (1, 2, 3, 4, 5, 6)
    #dice = (1, 2, 3, 4, 5, 5, 6)
    throw1 = choice(dice)
    throw2 = choice(dice)
    return throw1+throw2


def isAWin(result, point=-1, is2print=True):
    win1st = (7, 11)
    lose1st = (2, 3, 12)
    if(point > -1):
        if(result == 7):
            if(is2print):
                print('{},{}: you Lose!'.format(point, result))
            return 0
        elif(result == point):
            if(is2print):
                print('{},{}: you Win!'.format(point, result))
            return 1
        else:
            return isAWin(rollDice(), point, is2print)
    if(result in win1st):
        if(is2print):
            print('{}: you Win!'.format(result))
        return 1
    elif(result in lose1st):
        if(is2print):
            print('{}: you Lose!'.format(result))
        return 0
    else:
        point = result
        return isAWin(rollDice(), point, is2print)


def playCraps():
    wannaPlay = 'y'
    while(wannaPlay == 'y'):
        result = rollDice()
        isAWin(result)
        wannaPlay = input('Keep playing (y or n)?')
    print('Goodbye...')

# playCraps()


def playCrapsTrial(numThrows):
    wins, looses = 0, 0
    for i in range(numThrows):
        if(isAWin(rollDice(), is2print=False) == 1):
            wins += 1
        else:
            looses += 1
    print('Wins:', wins, 'Looses:', looses)
    print('House winning %:', float(looses)/float(wins+looses)*100)
    print('House looses %:', float(wins)/float(wins+looses)*100)


playCrapsTrial(100000)
