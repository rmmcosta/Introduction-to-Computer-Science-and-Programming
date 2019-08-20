def mySimpleSort(theList):
    assert len(theList)>0, 'you must pass a valid list'
    currLength = len(theList)
    result = []
    while currLength>0:
        currValue = theList[0]
        for i in range(currLength):
            if(theList[i]<currValue):
                currValue = theList[i]
            #print(currValue)                
        result.append(currValue)
        #print(currValue)
        #print(theList)
        theList.remove(currValue)
        #recalculate the length of the list
        currLength = len(theList)
    return result

def testMySimpleSort():
    l1 = [4,5,1,3,9,13,8]
    print(l1)
    print(mySimpleSort(l1))
    l2 = [1,2,3,4,5]
    print(l2)
    print(mySimpleSort(l2))
    l3 = [10,9,8,7,6,5,4,3,2,1,0]
    print(l3)
    print(mySimpleSort(l3))
    l4 = list(range(100,0,-2))
    print(l4)
    print(mySimpleSort(l4))

def selectionSort(theList):
    #use two cycles to run through the list
    listLen = len(theList)
    for i in range(listLen):
        minIdx = i
        minValue = theList[i]
        for j in range(i,listLen):
            if(theList[j]<minValue):
                minIdx = j
                minValue = theList[j]
        print(theList)
        theList[minIdx] = theList[i]
        theList[i]=minValue
         
def testSelectionSort():
    l1 = [4,5,1,3,9,13,8]
    print(l1)
    selectionSort(l1)
    print(l1)
    l2 = [1,2,3,4,5]
    print(l2)
    selectionSort(l2)
    print(l2)
    l3 = [10,9,8,7,6,5,4,3,2,1,0]
    print(l3)
    selectionSort(l3)
    print(l3)
    l4 = list(range(100,0,-2))
    print(l4)
    selectionSort(l4)
    print(l4)

def bubbleSort(theList):
    listLength = len(theList)
    for i in range(listLength):
        for j in range(listLength-1):
            if(theList[j]>theList[j+1]):
                temp = theList[j]
                theList[j]=theList[j+1]
                theList[j+1] = temp
                #print(theList)
                #input()

def testBubbleSort():
    l1 = [4,5,1,3,9,13,8]
    print(l1)
    bubbleSort(l1)
    print(l1)
    l2 = [1,2,3,4,5]
    print(l2)
    bubbleSort(l2)
    print(l2)
    l3 = [10,9,8,7,6,5,4,3,2,1,0]
    print(l3)
    bubbleSort(l3)
    print(l3)

def bubbleSortOptim(theList):
    listLength = len(theList)
    swaps = False
    for i in range(listLength):
        for j in range(listLength-1):
            if(theList[j]>theList[j+1]):
                swaps = True
                temp = theList[j]
                theList[j]=theList[j+1]
                theList[j+1] = temp
                print(theList)
                input()
        if(not swaps):
            return
                

def testBubbleSortOptim():
    l1 = [4,5,1,3,9,13,8]
    print(l1)
    bubbleSortOptim(l1)
    print(l1)
    l2 = [1,2,3,4,5]
    print(l2)
    bubbleSortOptim(l2)
    print(l2)
    l3 = [10,9,8,7,6,5,4,3,2,1,0]
    print(l3)
    bubbleSortOptim(l3)
    print(l3)
