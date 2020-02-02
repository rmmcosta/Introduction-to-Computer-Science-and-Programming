from randomWalkSimulation import Drunk, Chart

d1 = Drunk('John Borrachon', 0, 0)
d1.sayHi()

d2 = Drunk('Carlos', 0, 0)
d3 = Drunk('Hector', 0, 0)

for i in range(500):
    d1.move()
    d2.move()
    d3.move()

d1.sayHi()

# d1.printLocations()
# d1.printDistances()

c1 = Chart()
c1.addPlot(d1.getDistances())
c1.addPlot(d2.getDistances())
c1.addPlot(d3.getDistances())

c1.show('Distances', 'time', 'distance from origin')

# c2 = Chart()
# c2.addPlot(d1.getLocations())
# c2.show('Locations','time','current location')
