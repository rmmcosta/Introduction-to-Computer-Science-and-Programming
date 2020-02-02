from random import uniform, randint
from matplotlib import pyplot as plt
from datetime import datetime
from numpy import array, polyfit
from statistics import mean


def generateData(numSamples):
    # f(x) = a*x² + b*x + c
    a = uniform(0.0, 10.0)
    b = uniform(0.0, 10.0)
    c = uniform(0.0, 10.0)
    f = open("parabolaData.txt", "w+")
    # f.truncate(0)
    f.write('#a={}, b={}, c={} {}\n'.format(
        a, b, c, datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    f.write('#x:#F(x)\n')
    # starting putting samples on the file
    for x in range(numSamples):
        F = a*x*x + b*x + c
        # add a randomness
        choice = randint(0, 1)
        if(choice == 1):
            F += F*uniform(0.05, 0.2)
        else:
            F -= F*uniform(0.05, 0.2)
        f.write('{}:{}\n'.format(x, F))
    f.close()

def rSquare(estimated, measured):
    #estimated and measured must be arrays
    #if they are arrays already it will not make difference
    estimated = array(estimated)
    measured = array(measured)
    #calculate R²
    # R² = 1 - EE/DV
    #EE = sum((estimated(i) - measured(i))²)
    ee = (estimated-measured)**2
    ee = ee.sum()
    #DV = sum((measured(i)-mean_measured)²)
    theMean = mean(measured)
    dv = (measured-theMean)**2
    dv = dv.sum()
    R2 = 1 - (ee/dv)
    return R2

def calculateLinearRegression():
    f = open("parabolaData.txt", "r")
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
            force = float(values[1])
            distances.append(distance)
            forces.append(force)
    f.close()

    plt.scatter(distances, forces, color='blue')
    # in order to do operations with lists we need to convert them to arrays
    distances = array(distances)
    # let's choose degree 2 -> f(x) = a*x² + b*x + c
    a, b, c = polyfit(distances, forces, 2)
    print(a, b, c)
    ys = a*distances*distances + b*distances + c
    plt.plot(distances, ys, color='red')

    #print R2
    print('R2 for quadratic:',rSquare(ys,forces))
    
    #also a degree one
    a, b = polyfit(distances, forces, 1)
    print(a, b)
    ys = a*distances + b
    plt.plot(distances, ys, color='black')
    
    #print R2
    print('R2 for linear:',rSquare(ys,forces))

    plt.show()


generateData(100)
calculateLinearRegression()
