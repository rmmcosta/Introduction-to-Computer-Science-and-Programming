def getFibonacci(pos):
    '''returns true if the posber passed belongs to the Fibonacci sequence'''
    print('Fibo called for ',pos)
    if(pos==0 or pos==1):
        return pos
    else:
        return getFibonacci(pos-1)+getFibonacci(pos-2) 
