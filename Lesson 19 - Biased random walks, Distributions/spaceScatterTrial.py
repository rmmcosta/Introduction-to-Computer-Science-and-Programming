import sys

sys.path.insert(0, '/home/rmmcosta/Documents/Introduction to Computer Science and Programming/Lesson 17 - Computational Models: Random walk simulation/MySolution')

# print(sys.path)
from randomWalkSimulation import Drunk, SpaceDirection, Direction
from specialDrunks import *
import pylab

def drawScatter(maxTime, numTrials):
    #get the list of the final distances
    xAndyList = runSimulationScatter(maxTime, numTrials)
    pylab.scatter(0,0,color='r')
    pylab.scatter(xAndyList[0],xAndyList[1])
    xAndyList = runSimulationScatter(maxTime, numTrials, Drunk, SpaceDirection)
    pylab.scatter(xAndyList[0],xAndyList[1],color='r')
    pylab.xlabel('Distance in the x axis')
    pylab.ylabel('Distance in the y axis')

    #cold drunk
    pylab.figure('cold drunk')
    xAndyList = runSimulationScatter(maxTime, numTrials, ColdDrunk)
    pylab.scatter(0,0,color='r')
    pylab.scatter(xAndyList[0],xAndyList[1])
    xAndyList = runSimulationScatter(maxTime, numTrials, ColdDrunk, SpaceDirection)
    pylab.scatter(xAndyList[0],xAndyList[1],color='r')

    #ew drunk
    pylab.figure('ew drunk')
    xAndyList = runSimulationScatter(maxTime, numTrials, EWDrunk)
    pylab.scatter(0,0,color='r')
    pylab.scatter(xAndyList[0],xAndyList[1])
    xAndyList = runSimulationScatter(maxTime, numTrials, EWDrunk, SpaceDirection)
    pylab.scatter(xAndyList[0],xAndyList[1],color='r')


    pylab.show()


def runSimulationScatter(time, trials, DrunkClass=Drunk, DirectionType=Direction):
    xAndyLists = []
    xlist = []
    ylist = []
    # do the trials
    for trial in range(trials):
        drunkTest = DrunkClass('Drunk ' + str(trial), 0, 0, DirectionType)
        # give time to the drunk to move
        for t in range(time):
            currCoordinates = drunkTest.move()
            # if(currCoordinates==(0,0)):
            #     print('I am home')
        # append to the list in the end
        finalDist = drunkTest.getCurrentCoordinates() #tuple with the x and the y distance
        #print(finalDist)
        xlist.append(finalDist[0])
        ylist.append(finalDist[1])
    xAndyLists.append(xlist)
    xAndyLists.append(ylist)
    return xAndyLists

drawScatter(500,400)