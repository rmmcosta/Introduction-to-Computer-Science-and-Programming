import sys

sys.path.insert(0, '/home/rmmcosta/Documents/Introduction to Computer Science and Programming/Lesson 17 - Computational Models: Random walk simulation/MySolution')

# print(sys.path)
from randomWalkSimulation import Drunk, SpaceDirection
import pylab
from specialDrunks import *

def drawDistribution(maxTime, numTrials):
    #get the list of the final distances
    finalDists = runSimulationFinalDistances(maxTime, numTrials)
    pylab.hist(finalDists, density=True, histtype='bar', rwidth=0.8)
    pylab.xlabel('final distances')
    pylab.ylabel('n.º of times')

    # cold drunk
    pylab.figure('Cold drunk')
    finalDists = runSimulationFinalDistances(maxTime, numTrials, ColdDrunk)
    pylab.hist(finalDists, density=True, histtype='bar', rwidth=0.8)

    #ew drunk
    pylab.figure('EW drunk')
    finalDists = runSimulationFinalDistances(maxTime, numTrials, EWDrunk)
    pylab.hist(finalDists, density=True, histtype='bar', rwidth=0.8)

    pylab.show()


def runSimulationFinalDistances(time, trials, DrunkClass=Drunk):
    finalDistances = []
    # do the trials
    for trial in range(trials):
        drunkTest = DrunkClass('Drunk ' + str(trial), 0, 0, SpaceDirection)
        # give time to the drunk to move
        for t in range(time):
            currCoordinates = drunkTest.move()
            # if(currCoordinates==(0,0)):
            #     print('I am home')            
        # append to the list in the end
        # use the distances in x getCurrentCoordinates()[0], in y getCurrentCoordinates()[1]
        # or the final distance getCurrentDistance()
        finalDistances.append(drunkTest.getCurrentDistance())
    return finalDistances

drawDistribution(500,400)