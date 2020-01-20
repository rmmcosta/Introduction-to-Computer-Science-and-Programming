numCalls = 0

def fillKnapsack(w,vol,val,i,aweight,avol):
    global numCalls
    numCalls = numCalls + 1
    #print('called with i:{}, aw:{}, avol:{}'.format(i,aweight,avol))
    #this is the internal function
    #to start filling the knapsack
    #the w is the vector (tuple or list) with the weights
    #the val is the vector (tuple or list) with the values
    #the i is the index
    #the aweight is the available weight
    #the avol is the available volume
    #the memo is the dictionary use to memorize
    #the scenarios already computed

    #let's implement the recursion
    #first start by the base case (leafs)
    #if it's a leaf (decision tree)
    if(i==0):
        #still have room for the volume and the weight
        if(aweight >= w[i] and avol >= vol[i]):
            #take it
            return val[i]
        else:
            return 0
    else:
        #if it's not a leaf we have 2 options
        #take or not take and go from there
        
        #the not take will be reused
        #so let's put it in a variable
        notTake = fillKnapsack(w,vol,val,i-1,aweight,avol)

        #still have room for the volume and the weight
        if(aweight >= w[i] and avol >= vol[i]):
            #see the max between take it and don't take it
            take = val[i] + fillKnapsack(w,vol,val,i-1,aweight-w[i],avol-vol[i])
            return max(notTake,take)
        else:
            return notTake

def fastFillKnapsack(w,vol,val,i,aweight,avol,memo):
    global numCalls
    numCalls = numCalls + 1
    #print('memo',memo)
    #this is the internal function
    #to start filling the knapsack
    #the w is the vector (tuple or list) with the weights
    #the val is the vector (tuple or list) with the values
    #the i is the index
    #the aweight is the available weight
    #the avol is the available volume
    #the memo is the dictionary use to memorize
    #the scenarios already computed

    #check memory
    #return the max computation from memory or
    #save the max computation in memory
    key = '{},{},{}'.format(i,aweight,avol)
    if(key in memo):
        return memo.get(key)

    #let's implement the recursion
    #first start by the base case (leafs)
    #if it's a leaf (decision tree)
    if(i==0):
        #still have room for the volume and the weight
        if(aweight >= w[i] and avol >= vol[i]):
            #take it
            memo[key] = val[i]
            return val[i]
        else:
            memo[key] = 0
            return 0
    else:
        #if it's not a leaf we have 2 options
        #take or not take and go from there
        
        #the not take will be reused
        #so let's put it in a variable
        notTake = fastFillKnapsack(w,vol,val,i-1,aweight,avol,memo)

        #still have room for the volume and the weight
        if(aweight >= w[i] and avol >= vol[i]):
            #see the max between take it and don't take it
            take = val[i] + fastFillKnapsack(w,vol,val,i-1,aweight-w[i],avol-vol[i],memo)
            memo[key] = max(notTake,take)
            return memo.get(key)
        else:
            memo[key] = notTake
            return notTake


def goFillKnapsack():
    #wrapper for the fillKnapsack function
    #let's use tuples for the w and v vectors
    #tuples unlike list are immutable
    #tuples uses () and lists []
    w = (4,5,1)
    vol = (1,3,2)
    val = (3,6,2)
    i = len(w)-1
    aw = 5
    avol = 3
    memo = {}
    #restart numCalls
    global numCalls
    numCalls = 0
    maxVal = fillKnapsack(w,vol,val,i,aw,avol)
    print(maxVal)
    print('numCalls',numCalls)
    print('memoization version')
    numCalls = 0
    maxVal = fastFillKnapsack(w,vol,val,i,aw,avol,memo)
    print(maxVal)
    print('numCalls',numCalls)

def goFillKnapsack1():
    #wrapper for the fillKnapsack function
    #let's use tuples for the w and v vectors
    #tuples unlike list are immutable
    #tuples uses () and lists []
    w = (4,5,1,3,7,14,12)
    vol = (1,3,2,10,5,7,8)
    val = (3,6,2,44,22,1,33)
    i = len(w)-1
    aw = 10
    avol = 12
    memo = {}
    #restart numCalls
    global numCalls
    numCalls = 0
    maxVal = fillKnapsack(w,vol,val,i,aw,avol)
    print(maxVal)
    print('numCalls',numCalls)
    print('memoization version')
    numCalls = 0
    maxVal = fastFillKnapsack(w,vol,val,i,aw,avol,memo)
    print(maxVal)
    print('numCalls',numCalls)

def goFillKnapsack2():
    #wrapper for the fillKnapsack function
    #let's use tuples for the w and v vectors
    #tuples unlike list are immutable
    #tuples uses () and lists []
    w = (4,5,1,3,7,14,12,14,12)
    vol = (1,3,2,10,5,7,8,7,8)
    val = (3,6,2,44,22,1,33,1,33)
    i = len(w)-1
    aw = 10
    avol = 12
    memo = {}
    #restart numCalls
    global numCalls
    numCalls = 0
    maxVal = fillKnapsack(w,vol,val,i,aw,avol)
    print(maxVal)
    print('numCalls',numCalls)
    print('memoization version')
    numCalls = 0
    maxVal = fastFillKnapsack(w,vol,val,i,aw,avol,memo)
    print(maxVal)
    print('numCalls',numCalls)

def goFillKnapsack3():
    #wrapper for the fillKnapsack function
    #let's use tuples for the w and v vectors
    #tuples unlike list are immutable
    #tuples uses () and lists []
    w = (4,5,1,3,7,14,12,4,5,3,7)
    vol = (1,3,2,10,5,7,8,1,3,10,5)
    val = (3,6,2,44,22,1,33,3,6,44,22)
    i = len(w)-1
    aw = 10
    avol = 12
    memo = {}
    #restart numCalls
    global numCalls
    numCalls = 0
    maxVal = fillKnapsack(w,vol,val,i,aw,avol)
    print(maxVal)
    print('numCalls',numCalls)
    print('memoization version')
    numCalls = 0
    maxVal = fastFillKnapsack(w,vol,val,i,aw,avol,memo)
    print(maxVal)
    print('numCalls',numCalls)


