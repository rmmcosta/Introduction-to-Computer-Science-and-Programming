import sys

sys.path.insert(0, '/home/rmmcosta/Documents/Introduction to Computer Science and Programming/Lesson 17 - Computational Models: Random walk simulation/MySolution')

# print(sys.path)
from randomWalkSimulation import Drunk, SpaceDirection
from random import randint

class ColdDrunk(Drunk):
    #a drunk that preferes south
    def move(self):
        choice = randint(1,4)
        
        if(choice==1):
            self._direction.goNorth(self._location,self._step)
        elif(choice==2):
            self._direction.goSouth(self._location,self._step+self._step)
        elif(choice==3):
            self._direction.goEast(self._location,self._step)
        else:
            self._direction.goWest(self._location,self._step)

        self._locations.append(self._location.getCurrentCoordinates())
        self._distances.append(self._location.getCurrentDistance())
        
        return self._location.getCurrentDistance() 

class EWDrunk(Drunk):
    #a drunk that only goes east or west
    def move(self):
        choice = randint(1,2)

        if(choice==1):
            self._direction.goEast(self._location,self._step)
        else:
            self._direction.goWest(self._location,self._step)

        self._locations.append(self._location.getCurrentCoordinates())
        self._distances.append(self._location.getCurrentDistance())
        
        return self._location.getCurrentDistance()

class SpaceDrunk(Drunk):
    #a drunk that sometimes jumps home
    def move(self):
        if(type(self._direction)==SpaceDirection):
            choice = randint(1,5)
        else:
            choice = randint(1,4)
        
        if(choice==1):
            self._direction.goNorth(self._location,self._step)
        elif(choice==2):
            self._direction.goSouth(self._location,self._step+self._step)
        elif(choice==3):
            self._direction.goEast(self._location,self._step)
        elif(choice==4):
            self._direction.goWest(self._location,self._step)
        else:
            self._direction.goHome(self._location)

        self._locations.append(self._location.getCurrentCoordinates())
        self._distances.append(self._location.getCurrentDistance())
        
        return self._location.getCurrentDistance() 