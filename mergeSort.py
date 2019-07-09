def merge(left,right):
    result = []
    lenLeft = len(left)
    lenRight = len(right)
    i,j = 0,0
    while(i<lenLeft and j<lenRight):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #now we need to append the left numbers in one of the lists
    while(i<lenLeft):
        result.append(left[i])
        i+=1
    while(j<lenRight):
        result.append(right[j])
        j+=1
    return result

def mergeSort(theList):
    '''Sort and return the inputed list'''
    print('mergesort')
    print(theList)
    listLen = len(theList)

    if(listLen==1):
        return theList

    m=int(listLen/2)

    left = mergeSort(theList[:m])
    right = mergeSort(theList[m:])

    together = merge(left,right)
    print('merged', together)

    return together
    
