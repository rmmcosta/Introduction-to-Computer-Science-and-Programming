''' this solution doesn't work for every case
    it's just for some scenarios '''

numcalls = 0

def knapsack(weights,values,bagcapacity):
    assert len(weights) == len(values), 'the tuples must have the same size. weights {}, values {}'.format(len(weights),len(values))
    initialidx = len(weights)-1
    global numcalls
    numcalls = numcalls + 1
    possibilities = ()
    finalvalue = fillknapsack(bagcapacity,initialidx,bagcapacity,0,weights,values,possibilities)
    print(finalvalue)

def fillknapsack(bagcapacity,curridx,weightleft,accvalues,weights,values,possibilities):
    global numcalls
    numcalls = numcalls + 1
    if curridx < 0:
        possibilities = concat_tups(possibilities,accvalues)
        return max(possibilities)
    else:
        if weightleft == 0:
            weightleft = bagcapacity
            possibilities = concat_tups(possibilities,accvalues)
            accvalues = 0
        currvalue = values[curridx]
        currweight = weights[curridx]
        curridx = curridx - 1
        if currweight <= weightleft:
            return fillknapsack(bagcapacity,curridx,weightleft-currweight,accvalues+currvalue,weights,values,possibilities)
        else:
            return fillknapsack(bagcapacity,curridx,weightleft,accvalues,weights,values,possibilities)

def concat_tups(x,y):
##    print('concat_tups')
##    print(x)
##    print(y)
    return x + (y if isinstance(y,tuple) else (y,))

def testKnapsack():
    global numcalls
    numcalls=0
    w = (5,3,2)
    v = (9,7,8)
    b = 5
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapsack1():
    global numcalls
    numcalls=0
    w = (5,3,2,10,15)
    v = (9,7,8,20,18)
    b = 15
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapsack2():
    global numcalls
    numcalls=0
    w = (1,5,3,4)
    v = (15,10,9,5)
    b = 8
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapsack3():
    global numcalls
    numcalls=0
    w = (1,1,5,5,3,3,4,4)
    v = (15,15,10,10,9,9,5,5)
    b = 8
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapsack4():
    global numcalls
    numcalls=0
    w = (1,1,5,5,3,3,4,4)
    v = (15,15,10,10,9,9,5,5)
    b = 40
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapsack5():
    global numcalls
    numcalls=0
    w = (1,1,5,5,3,3,4,4,7,6,10,8,1,3,21,12,54,43,1,6,8,9,10,11,12,4,39,38,15)
    v = (15,15,10,10,9,9,5,5,11,12,34,12,1,21,45,54,600,1,23,25,1,2,0,10,100,23,2,37,54)
    b = 40
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)

def testKnapsack6():
    global numcalls
    numcalls=0
    w = (1,1,5,5,9,3,3,4,4)
    v = (150,15,10,10,500,9,9,5,5)
    b = 10
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)
