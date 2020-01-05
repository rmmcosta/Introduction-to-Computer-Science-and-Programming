def exponent(a,b):
    result = a
    if(b==0):
        return 1
    for i in range(b-1):
        #print(i)
        #print(result)
        result*=a
    return result

def exponent1(a,b):
    result = 1
    for i in range(b):
        #print(i)
        #print(result)
        result*=a
    return result

def expRecursive(a,b):
    if(b==0):
        return 1
    if(b==1):
        return a
    else:
        return a*expRecursive(a,b-1)

def expEvenOdd(a,b):
    if(b==0):
        return 1
    if(b==1):
        return a
    if(b%2==0):
        return expEvenOdd(a*a,b/2)
    else:
        return a*expEvenOdd(a,b-1)

def callTestExps():
    print('--- exponent ---')
    testExpsByMethod(exponent)
    print('--- exponent1 ---')
    testExpsByMethod(exponent1)
    print('--- expRecursive ---')
    testExpsByMethod(expRecursive)
    print('--- ExpEvenOdd ---')
    testExpsByMethod(expEvenOdd)

def testExpsByMethod(method):
    print('2⁰')
    print(method(2,0))
    print('2²')
    print(method(2,2))
    print('2³')
    print(method(2,3))
    print('2⁸')
    print(method(2,8))
    print('2⁹')
    print(method(2,9))
    print('2¹0')
    print(method(2,10))
    print('3²')
    print(method(3,2))
    print('4²')
    print(method(4,2))
