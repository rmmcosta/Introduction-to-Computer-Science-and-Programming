from random import uniform, randint
from statistics import mean
from matplotlib import pyplot as plt
from datetime import datetime
from numpy import array, polyfit

def generateData(numSamples):
    k = uniform(0.0,10.0)
    f = open("springData.txt", "w+")
    #f.truncate(0)
    f.write('#k={}, {}\n'.format(k, datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    f.write('#x:#F\n')
    #starting putting samples on the file
    for i in range(numSamples):
        x = uniform(1.0,20.0)
        F = -k*x
        #add a randomness
        choice = randint(0,1)
        if(choice==1):
            F += uniform(-k,k)
        else:
            F -= uniform(-k,k)
        f.write('{}:{}\n'.format(x,F))
    f.close()

def calculateK():
    f = open("springData.txt","r")
    kEstimates = []
    distances = []
    forces = []
    lines = f.readlines()
    for line in lines:
        isToIgnore = line.find('#') > -1
        if(isToIgnore):
            continue
        else:
            values = line.split(':')
            distance = float(values[0])
            force = -float(values[1])
            kEstimate = force/distance
            kEstimates.append(kEstimate)
            distances.append(distance)
            forces.append(force)
    f.close()

    meanValue = mean(kEstimates)
    print('first guess:',meanValue)
    #print(kEstimates)
    plt.plot(kEstimates)
    plt.xscale('log')
    plt.axhline(y=meanValue)
    plt.figure()
    plt.scatter(distances, forces)
    #let's choose degree 1 -> y=a*x+b
    a,b = polyfit(distances, forces, 1)
    print(a,b)
    distances = array(distances)
    ys = a*distances+b
    print('k based on the polyfit:', ys[0]/distances[0])
    plt.plot(distances,ys,color='red')
    plt.show()

    

generateData(100)
calculateK()