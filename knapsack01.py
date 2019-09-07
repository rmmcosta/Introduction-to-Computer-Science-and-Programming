numcalls = 0

def knapsack(weights,values,bagcapacity):
    """ given the weights tuple,
        the values tuple
        and the bag capacity
        it returns the best items to take """
    assert(len(weights) == len(values)), 'number of elements don\'t match'

    global numcalls
    numcalls+=1

    currW = bagcapacity
    currV = 0
    currIdx = len(weights)-1
    finallist = []
    t = (currIdx,currW,currV)
    intermlist = []
    intermlist.append(t)
    print('initial tuple')
    print(t)
    take(currW,currV,currIdx,weights,values,bagcapacity,finallist,intermlist)
    intermlist = []
    intermlist.append(t)
    print('initial tuple')
    print(t)
    nottake(currW,currV,currIdx,weights,values,bagcapacity,finallist,intermlist)
    #print(intermlist)
    print('end')
    print(finallist)

    maxvalue = 0
    finalpossibility = []

    for possibility in finallist:
        lastiter = len(possibility)-1
        finalvalue = possibility[lastiter][2]
        if finalvalue > maxvalue:
            maxvalue = finalvalue
            finalpossibility.clear()
            finalpossibility = possibility

    print('finalpossibility')
    print(finalpossibility)
    print('maxvalue')
    print(maxvalue)
        
    

def take(availW,accV,currIdx,weights,values,bagcapacity,finallist,intermlist):
    print('take')
    global numcalls
    numcalls+=1
    if currIdx > -1:
        currW = weights[currIdx]
        currV = values[currIdx]

        currIdx-=1
        
        if(currW<=availW):
            availW-=currW
            accV+=currV
            t = (currIdx,availW,accV)
            print('tuple')
            print(t)
            intermlist.append(t)
        
        take(availW,accV,currIdx,weights,values,bagcapacity,finallist,intermlist)
        intermlist = []
        nottake(availW,accV,currIdx,weights,values,bagcapacity,finallist,intermlist)
        intermlist = []
    else:
        print('leaf')
        if len(intermlist)>0:
            if intermlist[0][0] > -1:
                t = (currIdx,availW,accV)
                print('tuple')
                print(t)
                intermlist.append(t)
                #print('intermlist')
                #print(intermlist)
            finallist.append(intermlist)
        intermlist = []
        

def nottake(availW,accV,currIdx,weights,values,bagcapacity,finallist,intermlist):
    print('nottake')
    global numcalls
    numcalls+=1
    if currIdx > -1:
        
        currIdx-=1
        
        take(availW,accV,currIdx,weights,values,bagcapacity,finallist,intermlist)
        intermlist = []
        nottake(availW,accV,currIdx,weights,values,bagcapacity,finallist,intermlist)
        intermlist = []
    else:
        intermlist = []
        
def testKnapSack():
    global numcalls
    numcalls=0
    w = (5,3,2)
    v = (9,7,8)
    b = 5
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapSack1():
    global numcalls
    numcalls=0
    w = (5,3,2,10,15)
    v = (9,7,8,20,18)
    b = 15
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapSack2():
    global numcalls
    numcalls=0
    w = (1,5,3,4)
    v = (15,10,9,5)
    b = 8
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapSack3():
    global numcalls
    numcalls=0
    w = (1,1,5,5,3,3,4,4)
    v = (15,15,10,10,9,9,5,5)
    b = 8
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapSack3():
    global numcalls
    numcalls=0
    w = (1,1,5,5,3,3,4,4)
    v = (15,15,10,10,9,9,5,5)
    b = 40
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)
