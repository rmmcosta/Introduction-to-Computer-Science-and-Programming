import sys

sys.path.insert(0, '/home/rmmcosta/Documents/Introduction to Computer Science and Programming/Lesson 17 - Computational Models: Random walk simulation/MySolution')

# print(sys.path)
from randomWalkSimulation import Drunk, Chart, SpaceDirection
from specialDrunks import *
from random import randint

def ansQuest(maxTime, numTrials):
    #usual drunk
    means = []
    distLists = runSimulationReturnDistances(maxTime, numTrials, Drunk)
    #calculate the means for each time
    for t in range(maxTime):
        tot = 0.0
        #tot corresponds to the sum of each t value
        for dists in distLists:
            tot += dists[t]
        means.append(tot/len(distLists))
    chart = Chart()
    chart.addPlot(means,'usual drunk')

    #cold drunk
    means = []
    distLists = runSimulationReturnDistances(maxTime, numTrials, ColdDrunk)
    #calculate the means for each time
    for t in range(maxTime):
        tot = 0.0
        #tot corresponds to the sum of each t value
        for dists in distLists:
            tot += dists[t]
        means.append(tot/len(distLists))
    chart = Chart()
    chart.addPlot(means, 'cold drunk')

    #EW drunk
    means = []
    distLists = runSimulationReturnDistances(maxTime, numTrials, EWDrunk)
    #calculate the means for each time
    for t in range(maxTime):
        tot = 0.0
        #tot corresponds to the sum of each t value
        for dists in distLists:
            tot += dists[t]
        means.append(tot/len(distLists))
    chart = Chart()
    chart.addPlot(means, 'ew drunk')

    chart.show('Average of distances, {} trials'.format(numTrials),'time','distance',True) 


def runSimulationReturnDistances(time, trials, DrunkClass):
    distancesList = []
    # do the trials
    for trial in range(trials):
        drunkTest = DrunkClass('Drunk ' + str(trial), 0, 0, SpaceDirection)
        # give time to the drunk to move
        for t in range(time):
            drunkTest.move()
        # append to the list in the end
        distancesList.append(drunkTest.getDistances())
    return distancesList

ansQuest(500,400)
