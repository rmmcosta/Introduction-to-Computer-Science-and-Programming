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
            print 'iterations:'+str(i+1)
            return guess
        else:
            if(dev > 0):
                guess-=guess/2
            else:
                guess+=guess/2
    return 'Error. No square root found!'

def epsilon(deviation,eps):
    if(abs(deviation)<eps):
        return True
    else:
        return False
    
def deviation(x,y):
    return x*x-y

def sqrtBi(num,precision):
    MAX = 100
    assert num>=0, 'the number can not be negative'
    assert precision>0, 'the precision must be positive'
    low = 0
    high = num
    guess = (low+high)/2.0
    for i in range(MAX):
        dev = deviation(guess,num)
        if(epsilon(dev,precision)):
            print 'iterations:' + str(i+1)
            return guess
        if(dev<0):
            low = guess
        else:
            high = guess
        guess = (low+high)/2.0