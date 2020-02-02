from random import randint
from math import sqrt
import pylab

class Location:
    def __init__(self,initx,inity):
        self._x = initx
        self._y = inity
        self._initx = initx
        self._inity = inity

    def getInitialCoordinates(self):
        return (self._initx, self._inity)

    def setCoordinates2Initial(self):
        self._x = self._initx
        self._y = self._inity

    def getCurrentCoordinates(self):
        return (self._x, self._y)

    #inc and dec methods

    def incX(self,steps):
        self._x += steps

    def incY(self,steps):
        self._y += steps 

    def decX(self,steps):
        self._x -= steps

    def decY(self,steps):
        self._y -= steps

    #preview methods that can be used to understand where the location will be 
    #after inc or dec in the given coordinates

    def previewIncX(self,steps):
        return self._x + steps

    def previewIncY(self,steps):
        return self._y + steps 

    def previewDecX(self,steps):
        return self._x - steps

    def previewDecY(self,steps):
        return self._y - steps

    def getCurrentDistance(self):
        distx = self._x - self._initx
        disty = self._y - self._inity
        return sqrt(distx**2+disty**2)

class Direction:
    def __init__(self,field):
        self._field = field

    def goNorth(self,location,steps):
        if(location.previewIncY(steps) <= self._field.getMaxY()):
            location.incY(steps)
        else:
            print('End of the field in Y reached!')

    def goSouth(self,location,steps):
        if(location.previewDecY(steps) >= self._field.getMinY()):
            location.decY(steps)
        else:
            print('Begin of the field in Y reached!')        

    def goEast(self,location,steps):
        if(location.previewIncX(steps) <= self._field.getMaxX()):
            location.incX(steps)
        else:
            print('End of the field in X reached!') 

    def goWest(self,location,steps):
        if(location.previewDecX(steps) >= self._field.getMinX()):
            location.decX(steps)
        else:
            print('Begin of the field in X reached!') 

class SpaceDirection(Direction):
    def goHome(self,location):
        location.setCoordinates2Initial()
        #print('go home')
        #print('location object', location)
        #print(location.getCurrentCoordinates())

    def shouldGoHome(self, location):
        #print('should go home')
        currCoordinates = location.getCurrentCoordinates()
        if(abs(currCoordinates[0])==abs(currCoordinates[1])):
            self.goHome(location)

    def goNorth(self, location, steps):
        super().goNorth(location, steps)
        self.shouldGoHome(location)

    def goSouth(self, location, steps):
        super().goSouth(location, steps)
        self.shouldGoHome(location)

    def goEast(self, location, steps):
        super().goEast(location, steps)
        self.shouldGoHome(location)

    def goWest(self, location, steps):
        super().goWest(location, steps)
        self.shouldGoHome(location)

class Field:
    def __init__(self,minx,miny,maxx,maxy):
        self._minx = minx
        self._miny = miny
        self._maxx = maxx
        self._maxy = maxy

    def getMaxX(self):
        return self._maxx
    
    def getMaxY(self):
        return self._maxy

    def getMinX(self):
        return self._minx

    def getMinY(self):
        return self._miny

class Drunk:

    def __init__(self, name, x, y, DirectionType=Direction):
        self._location = Location(x,y)
        #print('location object',self._location)
        self._name = name
        self._field = Field(-1000,-1000,1000,1000)
        self._direction = DirectionType(self._field)
        self._step = 1
        self._locations = ['0,0']
        self._distances = [0.0]

    def sayHi(self):
        print('My name is {}. I started at {} and now I am at {}'.format(self._name,self._location.getInitialCoordinates(),self._location.getCurrentCoordinates()))

    def move(self):
        choice = randint(1,4)
        
        if(choice==1):
            self._direction.goNorth(self._location,self._step)
        elif(choice==2):
            self._direction.goSouth(self._location,self._step)
        elif(choice==3):
            self._direction.goEast(self._location,self._step)
        else:
            self._direction.goWest(self._location,self._step)

        self._locations.append(self._location.getCurrentCoordinates())
        self._distances.append(self._location.getCurrentDistance())
        
        return self._location.getCurrentCoordinates()

    def printLocations(self):
        print(self._locations)

    def printDistances(self):
        print(self._distances)

    def getLocations(self):
        return self._locations

    def getDistances(self):
        return self._distances

    def getCurrentDistance(self):
        return self._location.getCurrentDistance()

    def getCurrentCoordinates(self):
        return self._location.getCurrentCoordinates()

class Chart:
    def __init__(self):
        self._pylab = pylab

    def addPlot(self,points,customLabel=''):
        self._pylab.plot(points,label=customLabel)

    def show(self, title, xaxisTitle, yaxisTitle, showLegend=False):
        self._pylab.title(title)
        self._pylab.xlabel(xaxisTitle)
        self._pylab.ylabel(yaxisTitle)
        
        if(showLegend):
            self._pylab.legend()

        self._pylab.show()
        

        