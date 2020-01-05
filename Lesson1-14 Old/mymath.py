def perfectsqrt(num):
    i=0
    while(i*i<num):
        i+=1
    if(i*i==num):
        return i
    else:
        return 'not a perfect square'

def realsqrt(num,eps):
    assert num>=0, 'the number must not be negative'
    assert eps>0, 'the precision must be positive'
    #initial guess
    guess = num/2.0
    for i in range(100):
        #print guess
        dev = deviation(guess,num)
        if(epsilon(dev,eps)):
            print('iterations:'+str(i+1))
            return guess
        else:
            if(dev > 0):
                guess-=guess/2
            else:
                guess+=guess/2
    return 'Error. No square root found!'

def testRealSqrt():
    print('testing realsqrt(4,0.2)')
    realsqrt(4,0.2)
    print('testing realsqrt(9,0.2)')
    realsqrt(9,0.2)
    print('testing realsqrt(2,0.2)')
    realsqrt(2,0.2)
    print('testing realsqrt(0.25,0.2)')
    realsqrt(0.25,0.2)

def epsilon(deviation,eps):
    if(abs(deviation)<eps):
        return True
    else:
        return False
    
def deviation(x,y):
    dev = x*x-y
    #print(dev)
    return dev

def sqrtBi(num,precision):
    MAX = 100
    assert num>=0, 'the number can not be negative'
    assert precision>0, 'the precision must be positive'
    low = 0
    high = num
    #the square root of numbers less than 1 is bigger than the number itself
    if(num<1):
        high = 1
    #we could also have done somthing like high = max(num,1)
    guess = (low+high)/2.0
    for i in range(MAX):
        dev = deviation(guess,num)
        if(epsilon(dev,precision)):
            print('iterations:' + str(i+1))
            return guess
        if(dev<0.0):
            low = guess
        else:
            high = guess
        guess = (low+high)/2.0

def testSqrtBi():
    print('testing sqrtBi(4,0.0001)')
    print(sqrtBi(4,0.0001))
    print('testing sqrtBi(9,0.0001)')
    print(sqrtBi(9,0.0001))
    print('testing sqrtBi(2,0.0001)')
    print(sqrtBi(2,0.0001))
    print('testing sqrtBi(0.25,0.0001)')
    print(sqrtBi(0.25,0.0001))

def sqrtNewton(num,precision):
    #finds the square root of a number using the newton method
    #f(guess)=guess²-x
    #given x=16 and guessi = 3 -> f(3)=9-16=-7
    #f(guess)=0
    #f'(guessi)=2*guessi
    #guessi+1=guessi - f(guessi)/2guessi
    #guessi+1=3-(-7/6)=25/6
    assert num>=0, 'the number must not be negative'
    assert precision, 'the precision must be a positive number'
    MAX = 100
    guessi = num/2
    for i in range(MAX):
        dev = deviation(guessi,num)
        if(epsilon(dev,precision)):
            print('iterations:'+str(i+1))
            return guessi
        else:
            guessi=guessi-(dev/(2*guessi))
    print('square root not found')

def testSqrtNewton():
    print('testing sqrtNewton(4,0.0001)')
    print(sqrtNewton(4,0.0001))
    print('testing sqrtNewton(9,0.0001)')
    print(sqrtNewton(9,0.0001))
    print('testing sqrtNewton(2,0.0001)')
    print(sqrtNewton(2,0.0001))
    print('testing sqrtNewton(0.25,0.0001)')
    print(sqrtNewton(0.25,0.0001))

def compareMethods():
    print('testing sqrt(2.0,0.01)')
    print('Newton Raphson method')
    print(sqrtNewton(2.0,0.01))
    print('Bi-section method')
    print(sqrtBi(2.0,0.01))
    input()
    print('testing sqrt(2.0,0.0001)')
    print('Newton Raphson method')
    print(sqrtNewton(2.0,0.0001))
    print('Bi-section method')
    print(sqrtBi(2.0,0.0001))
    input()
    print('testing sqrt(2.0,0.000001)')
    print('Newton Raphson method')
    print(sqrtNewton(2.0,0.000001))
    print('Bi-section method')
    print(sqrtBi(2.0,0.000001))
    input()
    print('testing sqrt(4.0,0.0001)')
    print('Newton Raphson method')
    print(sqrtNewton(4.0,0.0001))
    print('Bi-section method')
    print(sqrtBi(4.0,0.0001))
    input()
    print('testing sqrt(2.0,0.0001)')
    print('Newton Raphson method')
    print(sqrtNewton(2.0,0.0001))
    print('Bi-section method')
    print(sqrtBi(2.0,0.0001))
    input()
    print('testing sqrt(100.0,0.0001)')
    print('Newton Raphson method')
    print(sqrtNewton(100.0,0.000001))
    print('Bi-section method')
    print(sqrtBi(100.0,0.000001))
    input()
    print('testing sqrt(56.0,0.00000001)')
    print('Newton Raphson method')
    print(sqrtNewton(56.0,0.00000001))
    print('Bi-section method')
    print(sqrtBi(56.0,0.00000001))
    input()
    print('testing sqrt(123456789,0.0001)')
    print('Newton Raphson method')
    print(sqrtNewton(123456789,0.0001))
    print('Bi-section method')
    print(sqrtBi(123456789,0.0001))
    input()
    print('testing sqrt(123456789,0.000001)')
    print('Newton Raphson method')
    print(sqrtNewton(123456789,0.000001))
    print('Bi-section method')
    print(sqrtBi(123456789,0.000001))
    input()
