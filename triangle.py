from math import sqrt

def calcHypotenuse(a,b):
    return sqrt(a**2+b**2)

def calcHypotenuse2():
    a = input()
    b = input()
    assert str(a).isnumeric(), 'a must be a number'
    assert str(b).isnumeric(), 'b must be a number'
    a = int(a)
    b = int(b)
    assert a>0 and b>0, 'both a and b must be greater than zero'
    return calcHypotenuse(a,b)
