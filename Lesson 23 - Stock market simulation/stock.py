from matplotlib import pyplot as plt
from datetime import date, timedelta
from random import uniform, gauss


class Stock:
    _plt = plt
    def __init__(self, initPrice, numOfStocks, name, distribution, initDate=date.today()):
        self._initPrice = initPrice
        self._initDate = initDate
        self._currentDate = initDate
        self._numOfStocks = numOfStocks
        self._currentPrice = initPrice
        self._pricesHistory = [initPrice]
        self._datesHistory = [initDate]
        self._name = name
        self._distribution = distribution

    def buy(self, amount):
        pass

    def sell(self, amount):
        pass

    def increasePrice(self, percentage):
        pass

    def decreasePrice(self, percentage):
        pass

    def getNumOfStocks(self):
        return self._numOfStocks

    def getName(self):
        return self._name

    def getCurrentPrice(self):
        return self._currentPrice

    def getCurrentDate(self):
        return self._currentDate

    def setCurrentDate(self, newDate):
        self._currentDate = newDate

    def setCurrentPrice(self, newPrice, theDate=date.today()):
        self._currentPrice = newPrice
        self._pricesHistory.append(newPrice)
        self._datesHistory.append(theDate)
        self.setCurrentDate(theDate)

    def makeMove(self):
        newPrice = self.getCurrentPrice()*(1.0+self._distribution())
        newDate = self.getCurrentDate() + timedelta(days=1)
        self.setCurrentPrice(newPrice, theDate=newDate)

    def getInitialPrice(self):
        return self._initPrice

    def getDatesHistory(self):
        return self._datesHistory

    def getPricesHistory(self):
        return self._pricesHistory

    def getInitDate(self):
        return self._initDate

    def chartHistory():
        Stock._plt.title('Price history for the stock')
        Stock._plt.xlabel('Day')
        Stock._plt.ylabel('Price')
        #Stock._plt.legend()
        Stock._plt.show()

    def addChar(datesHistory, pricesHistory, name):
        Stock._plt.plot(datesHistory, pricesHistory, label = name)
        


def unitTestStock():
    # stock1 = Stock(2.0, 10000, 'My Stock', initDate=date(2020, 2, 8))
    # stock1.setCurrentPrice(2.1)
    # stock1.chartHistory()
    numOfStocks = 20
    numOfDays = 100
    stocks1, stocks2 = create2StoksLists(numOfStocks)
    runSim(stocks1, numOfDays)
    runSim(stocks2, numOfDays)

def runSim(stocks, numOfDays):
    for s in stocks:
        for i in range(numOfDays):
            s.makeMove()
        Stock.addChar(s.getDatesHistory(), s.getPricesHistory(), s.getName())
    Stock.chartHistory()
        

def create2StoksLists(numOfStocks):
    # lets create 2 types of lists
    # one for stocks with uniform distribution
    # another for stocks with gauss distribution
    stocks1 = []
    stocks2 = []

    for i in range(numOfStocks):
        volatility = uniform(0, 0.2)
        dist1 = lambda: uniform(-volatility, volatility)
        dist2 = lambda: gauss(0.0, volatility/2.0)
        initPrice = uniform(1.0, 10.0)
        randStockNum = uniform(1000,10000)
        stockName = 'stock{}'.format(i)
        stocks1.append(Stock(initPrice, randStockNum, stockName, dist1))
        stocks2.append(Stock(initPrice, randStockNum, stockName, dist2))

    return stocks1, stocks2
