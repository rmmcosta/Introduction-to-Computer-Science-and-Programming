import sys

sys.path.insert(0, '/home/rmmcosta/Documents/Introduction to Computer Science and Programming/Lesson 17 - Computational Models: Random walk simulation/MySolution')

# print(sys.path)
from randomWalkSimulation import Drunk
from specialDrunks import *
import pylab

def drawScatter(maxTime, numTrials):
    #get the list of the final distances
    xAndyList = runSimulationScatter(maxTime, numTrials)
    pylab.scatter(0,0,color='r')
    pylab.scatter(xAndyList[0],xAndyList[1])
    pylab.xlabel('Distance in the x axis')
    pylab.ylabel('Distance in the y axis')

    #cold drunk
    pylab.figure('cold drunk')
    xAndyList = runSimulationScatter(maxTime, numTrials, ColdDrunk)
    pylab.scatter(0,0,color='r')
    pylab.scatter(xAndyList[0],xAndyList[1])

    #ew drunk
    pylab.figure('ew drunk')
    xAndyList = runSimulationScatter(maxTime, numTrials, EWDrunk)
    pylab.scatter(0,0,color='r')
    pylab.scatter(xAndyList[0],xAndyList[1])

    pylab.show()


def runSimulationScatter(time, trials, DrunkClass=Drunk):
    xAndyLists = []
    xlist = []
    ylist = []
    # do the trials
    for trial in range(trials):
        drunkTest = DrunkClass('Drunk ' + str(trial), 0, 0)
        # give time to the drunk to move
        for t in range(time):
            drunkTest.move()
        # append to the list in the end
        finalDist = drunkTest.getCurrentCoordinates() #tuple with the x and the y distance
        #print(finalDist)
        xlist.append(finalDist[0])
        ylist.append(finalDist[1])
    xAndyLists.append(xlist)
    xAndyLists.append(ylist)
    return xAndyLists

drawScatter(500,400)