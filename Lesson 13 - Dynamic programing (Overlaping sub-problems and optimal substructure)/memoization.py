sumMemo = {
    '2,10':12,
    '3,2': 5,
    '2,3': 5
}

def getSumResult(x,y):
    global sumMemo
    calcStr = '{},{}'.format(x,y)
    if(calcStr in sumMemo):
        print('in memo')
        return sumMemo.get(calcStr)
    else:
        print('not in memo')
        sumMemo.update({calcStr:x+y})
        return sumMemo.get(calcStr)

def testSumResults():
    print(getSumResult(2,11))
    print(getSumResult(3,2))
    print(getSumResult(2,11))
