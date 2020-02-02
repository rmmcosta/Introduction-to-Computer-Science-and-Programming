import sys

sys.path.insert(0, '/home/rmmcosta/Documents/Introduction to Computer Science and Programming/Lesson 17 - Computational Models: Random walk simulation/MySolution')

# print(sys.path)
from randomWalkSimulation import Drunk, Chart

def runSimulation(times):
    drunkTest = Drunk('Test Drunk', 0, 0)
    for i in range(times):
        drunkTest.move()
    return drunkTest.getCurrentDistance()


def performTrial(numSamples, times):
    samples = []

    for i in range(numSamples):
        samples.append(runSimulation(times))

    return samples


def showTrial(numSamples, times):
    means = []
    samples = performTrial(numSamples, times)
    totalDistance = 0.0
    # calc total distances
    for sample in samples:
        totalDistance += sample
    print(totalDistance)
    totalSamples = len(samples)
    for i in range(totalSamples):
        means.append(totalDistance/totalSamples)
    chartTrial = Chart()
    chartTrial.addPlot(samples)
    chartTrial.addPlot(means)
    chartTrial.show('Samples', 'Number of samples', 'Distance')


def ansQuest(maxTime, numTrials):
    means = []
    distLists = runSimulationReturnDistances(maxTime, numTrials)
    #calculate the means for each time
    for t in range(maxTime):
        tot = 0.0
        #tot corresponds to the sum of each t value
        for dists in distLists:
            tot += dists[t]
        means.append(tot/len(distLists))
    chart = Chart()
    chart.addPlot(means)
    chart.show('Average of distances, {} trials'.format(numTrials),'time','distance') 


def runSimulationReturnDistances(time, trials):
    distancesList = []
    # do the trials
    for trial in range(trials):
        drunkTest = Drunk('Drunk ' + str(trial), 0, 0)
        # give time to the drunk to move
        for t in range(time):
            drunkTest.move()
        # append to the list in the end
        distancesList.append(drunkTest.getDistances())
    return distancesList
