from random import uniform
from math import sqrt
from matplotlib import pyplot as plt
from statistics import mean

class Board:
    def __init__(self, squareDimension):
        self._squareDimension = squareDimension

    def throwArrow(self):
        x = uniform(0,self._squareDimension)
        y = uniform(0,self._squareDimension)
        return x,y

    def isInsideCircle(self,x,y):
        #is inside circle if the hypotenuse for the x and y 
        #is less or equal to the square dimension
        h = sqrt(x*x + y*y)

        if(h <= self._squareDimension):
            return True
        else:
            return False

def calcPiTrial(boardSize, numThrows, numTrials, shouldPlot=True):
    board = Board(boardSize)
    pis = []
    pisOverTime = []
    for i in range(numTrials):
        pi = 0
        throwsIn = 0
        for j in range(numThrows):
            x,y = board.throwArrow()
            if(board.isInsideCircle(x,y)):
                throwsIn += 1
            piOverTime = 4*throwsIn/(j+1)
            pisOverTime.append(piOverTime)
        #pi is equal to the circunference
        #1/4 of the circunference is given roughly by the throws in ratio
        pi = 4*throwsIn/numThrows
        pis.append(pi)
    
    piEstimate = mean(pis)
    print(piEstimate)
    piEstimateOverTime = mean(pisOverTime)
    print(piEstimateOverTime)

    if(shouldPlot):
        #draw chart
        plt.plot(pis)
        plt.ylabel('Pi estimate')
        plt.xlabel('throws')
        #plt.xscale('log')
        plt.axhline(y=piEstimate)
    
        plt.figure()
        plt.plot(pisOverTime)
        plt.ylabel('Pi estimate')
        plt.xlabel('throws')
        plt.xscale('log')
        plt.axhline(y=piEstimateOverTime)

        plt.show()

calcPiTrial(1,100,100)

#calcPiTrial(1, 10000000, 1, False)