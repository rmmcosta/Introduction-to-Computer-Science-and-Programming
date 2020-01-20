import math
from abc import ABC, abstractmethod 
  
class Point(ABC): 
  
    # common method
    def __eq__(self, other): 
        print('from abstract eq')
        return self.x-other.x < 0.01 and self.y-other.y < 0.01
    
    # common method
    def cartesian(self):
        return 'x:{}, y:{}'.format(self.x, self.y)
    
    # common method
    def polar(self):
        return 'radius:{}, angle:{}'.format(self.radius, self.angle)

class CartesianPoint(Point):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = math.sqrt(x*x+y*y)
        self.angle = math.atan(y/x)
    # def __eq__(self,other):
    #     return self.x-other.x < 0.01 and self.y-other.y < 0.01

class PolarPoint(Point):
    def __init__(self,r,a):
        self.radius = r
        self.angle = a
        self.x = math.cos(a)*r
        self.y = math.sin(a)*r
    # def __eq__(self,other):
    #     return self.radius-other.radius < 0.01 and self.angle-other.angle < 0.01