import math

def findElem(list,elem):
    for i in range(len(list)):
        #print(list[i])
        #print(i)
        if(elem == list[i]):
            return True
        if(elem < list[i]):
            return False
    return False

def findElemOptim(list,elem):
    llength = len(list)
    l1 = list[math.ceil(llength/2):llength]
    l2 = list[0:math.ceil(llength/2)]
    return findElem(l1,elem) or findElem(l2,elem)

def findElemOptimFinal(list,elem):
    #print(list)
    min = 0
    max = len(list)
    guess = int((max-min)/2)
    #print('guess:'+str(guess))
    if list[guess] == elem:
        return True
    if max <= 1:
        return False
    if list[guess] < elem:            
        return findElemOptimFinal(list[guess+1:max],elem)
    else:
        return findElemOptimFinal(list[min:guess],elem)

def testFind():
    size=""
    while(not size.isdigit()):
        size=input('what is the size of list?')
    size = int(size)
    
    '''
    Use range. In Python 2.x it returns a list so all you need is:

    >>> range(11, 17)
    [11, 12, 13, 14, 15, 16]

    In Python 3.x range is a iterator. So, you need to convert it to a list:

    >>> list(range(11, 17))
    [11, 12, 13, 14, 15, 16]
    '''
    
    l1=list(range(0,size*2,2))
    print(l1)
    
    input()
    print('find 15')
    print(findElem(l1,15))
    input()
    print(findElemOptim(l1,15))
    input()
    print(findElemOptimFinal(l1,15))
    
    input()
    print('find 5')
    print(findElem(l1,5))
    input()
    print(findElemOptim(l1,5))
    input()    
    print(findElemOptimFinal(l1,5))
    
    input()
    print('find 4')
    print(findElem(l1,4))
    input()
    print(findElemOptim(l1,4))
    input()    
    print(findElemOptimFinal(l1,4))

    input()
    print('find 8')
    print(findElem(l1,8))
    input()
    print(findElemOptim(l1,8))   
    input() 
    print(findElemOptimFinal(l1,8))

    input()
    print('find 2')
    print(findElem(l1,2))
    input()
    print(findElemOptim(l1,2)) 
    input()   
    print(findElemOptimFinal(l1,2))
    
    input()
    print('find 10')
    print(findElem(l1,10))
    input()
    print(findElemOptim(l1,10)) 
    input()   
    print(findElemOptimFinal(l1,10))

    input()
    print('find 0')
    print(findElem(l1,0))
    input()
    print(findElemOptim(l1,0))   
    input() 
    print(findElemOptimFinal(l1,0))
    
    input()
    print('find 1')
    print(findElem(l1,1))
    input()
    print(findElemOptim(l1,1))    
    input()
    print(findElemOptimFinal(l1,1))

    input()
    print('find 9')
    print(findElem(l1,9))
    input()
    print(findElemOptim(l1,9))    
    input()
    print(findElemOptimFinal(l1,9))
