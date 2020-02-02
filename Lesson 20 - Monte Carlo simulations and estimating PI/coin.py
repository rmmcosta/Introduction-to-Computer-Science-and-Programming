from random import choice
import matplotlib.pyplot as plt
from statistics import mean


class Coin:
    # tuple with heads and tails
    options = ('heads', 'tails')

    def __init__(self):
        self._numTails = 0
        self._numHeads = 0

    def flip(self):
        result = choice(Coin.options)
        if(result == 'heads'):
            self._numHeads += 1
        else:
            self._numTails += 1
        return result

    def returnResults(self):
        return (self._numHeads, self._numTails)

    def printResults(self):
        print('Heads:{}, Tails:{}'.format(self._numHeads, self._numTails))

    def drawResults(self):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = Coin.options
        sizes = [self._numHeads, self._numTails]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

# c1 = Coin()
# c1.flip()
# c1.printResults()


def flipTrial(numFlips, numTrials):
    resultHeads = []
    resultTails = []
    diffs = []
    diffPercentages = []
    for j in range(numTrials):
        coinTest = Coin()
        for i in range(numFlips):
            coinTest.flip()
        #coinTest.printResults()
        #coinTest.drawResults()
        trialResult = coinTest.returnResults()
        heads = trialResult[0]
        tails = trialResult[1]

        resultHeads.append(heads)
        resultTails.append(tails)

        absDiff = abs(heads-tails)
        diffs.append(absDiff)
        diffPercentages.append(absDiff/numFlips)

    #draw the line chart for the results
    # plt.xlabel('heads')
    # plt.ylabel('tails')
    # plt.plot(resultHeads, resultTails)
    # plt.title('Heads vs Tails')

    #draw the line chart for the differences
    # plt.figure()
    # plt.plot(diffs)

    #draw the line chart for the difference percentages
    plt.figure()
    plt.plot(diffPercentages)
    plt.axhline(mean(diffPercentages), color='k', linestyle='dashed', linewidth=1)

    #draw an histogram
    plt.figure()
    plt.hist(diffs, rwidth=0.8)
    plt.axvline(mean(diffs), color='k', linestyle='dashed', linewidth=1)

    plt.show()
    
def flipTrialAllCoinsEqualResults(numCoins, numFlips, numTrials):
    equalResults = []
    probabilities = []
    for t in range(numTrials):
        numEqResults = 0
        coins = []
        for c in range(numCoins):
            coins.append(Coin())
        for f in range(numFlips):
            results = []
            for coin in coins:
                results.append(coin.flip())
            
            areAllEqual = all(r == results[0] for r in results)
            if(areAllEqual):
                numEqResults+=1
        equalResults.append(numEqResults)
        probabilities.append(numEqResults/numFlips*100)
    
    plt.plot(equalResults)
    plt.axhline(mean(equalResults), color='k', linestyle='dashed', linewidth=1)
    plt.figure()
    plt.plot(probabilities)
    plt.axhline(mean(probabilities), color='k', linestyle='dashed', linewidth=1)
    plt.show()


#flipTrial(3,4000)

flipTrialAllCoinsEqualResults(3,4000,100)
