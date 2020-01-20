import points
import math

##cp1 = points.CartesianPoint()
##cp2 = points.CartesianPoint()
##
##cp1.x = 1
##cp1.y = 2
##
##cp2.x = 3
##cp2.y = 5
##
##print(cp1)
##print(cp2)
##
##print(cp1.x,cp1.y)
##print(cp2.x,cp2.y)

cpa = points.CartesianPoint(5,5)
cpb = points.PolarPoint(7.0710678,math.pi/4)

print(cpa.cartesian(), cpa.polar())
print(cpb.cartesian(), cpb.polar())

print('cpa == cpb',cpa==cpb)
