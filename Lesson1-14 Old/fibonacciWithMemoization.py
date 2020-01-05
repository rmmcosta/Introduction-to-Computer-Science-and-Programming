fiboTimes = 0
fiboMemo = {
        0:0,
        1:1
    }


def printTimes():
    print(fiboTimes)

def calcFibo(num):
    incTimes()
    if(num==0):
        return 0
    if(num==1):
        return 1
    return calcFibo(num-1) + calcFibo(num-2)

def calcFiboWithMemo(num):
    incTimes()
    return getFiboMemo(num)

def getFiboMemo(num):
    global fiboMemo
    if(num in fiboMemo):
        return fiboMemo.get(num)
    else:
        fiboMemo.update({num:calcFiboWithMemo(num-1)+calcFiboWithMemo(num-2)})
        return fiboMemo.get(num)
        
def incTimes():
    global fiboTimes #because we will need to change the variable value 
    fiboTimes = fiboTimes+1

def testFibo():
    print('Which fibonacci you want to calculate?')
    num = input()
    if(num.isdigit()):
        global fiboTimes
        fiboTimes = 0
        print(calcFibo(int(num)))
        print(str(fiboTimes)+' calculations')
    else:
        print('You must input a number!')
    testFibo()

def testFiboWithMemo():
    print('Which fibonacci you want to calculate?')
    num = input()
    if(num.isdigit()):
        global fiboTimes
        fiboTimes = 0
        print(calcFiboWithMemo(int(num)))
        print(str(fiboTimes)+' calculations')
        print(fiboMemo)
        
    else:
        print('You must input a number!')
    testFiboWithMemo()
