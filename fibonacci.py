def getFibonacci(pos):
    '''returns true if the posber passed belongs to the Fibonacci sequence'''
    if(pos==0 or pos==1):
        return 1
    else:
        return isFibonacci(pos-1)+isFibonacci(pos-2) 