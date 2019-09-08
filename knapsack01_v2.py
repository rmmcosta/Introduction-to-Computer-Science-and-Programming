numcalls = 0
memo = {}


def knapsack(weights,values,bagcapacity):
    assert len(weights) == len(values),'the tuples must have the same size weights {} values {}'.format(len(weights),len(values))

    global numcalls
    numcalls+=1
    
    initialidx = len(weights)-1
    finalvalue = fillknapsack(weights,values,initialidx,bagcapacity)
    print(finalvalue)
    

def fillknapsack(w,v,i,aw):
    #print('called with: i = {} and aw = {}'.format(i,aw))
    global numcalls
    numcalls+=1
##    print('fillknapsack {} - {} - {} - {}'.format(w,v,i,aw))
    if i == 0:
##        print('end')
        if w[i] > aw:
            return 0
        else:
            return v[i]
    else:
        without_i = fillknapsack(w,v,i-1,aw)
        with_i = v[i]+fillknapsack(w,v,i-1,aw-w[i])
        if w[i] > aw:
            return without_i
        else:
            #print('max {},{}'.format(with_i,without_i))
            return max(with_i,without_i)

def knapsackwithmemo(weights,values,bagcapacity):
    assert len(weights) == len(values),'the tuples must have the same size weights {} values {}'.format(len(weights),len(values))

    global numcalls
    numcalls+=1
    
    initialidx = len(weights)-1
    finalvalue = fillknapsackwithmemo(weights,values,initialidx,bagcapacity,{})
    print(finalvalue)

def fillknapsackwithmemo(w,v,i,aw,m):
    #print(m)
    #print('called with: i = {} and aw = {}'.format(i,aw))
    global numcalls
    numcalls+=1
##    print('fillknapsack {} - {} - {} - {}'.format(w,v,i,aw))
    key = (i,aw)
    if key in m:
        #print('memo used')
        return m[key]
    if i == 0:
##        print('end')
        if w[i] > aw:
            m[key] = 0
            return 0
        else:
            m[key] = v[i]
            return v[i]
    else:
        without_i = fillknapsackwithmemo(w,v,i-1,aw,m)
        with_i = v[i]+fillknapsackwithmemo(w,v,i-1,aw-w[i],m)
        if w[i] > aw:
            m[key] = without_i
            return without_i
        else:
            temp = max(with_i,without_i)
            m[key] = temp
            return temp
    

def testKnapsack():
    global numcalls
    numcalls=0
    w = (5,3,2)
    v = (9,7,8)
    b = 5
    knapsack(w,v,b)
    print('total calls:')
    print(numcalls)
    numcalls = 0
    knapsackwithmemo(w,v,b)
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
    numcalls = 0
    knapsackwithmemo(w,v,b)
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
    numcalls = 0
    knapsackwithmemo(w,v,b)
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
    numcalls = 0
    knapsackwithmemo(w,v,b)
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
    numcalls = 0
    knapsackwithmemo(w,v,b)
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
    numcalls = 0
    knapsackwithmemo(w,v,b)
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
    numcalls = 0
    knapsackwithmemo(w,v,b)
    print('total calls:')
    print(numcalls)
