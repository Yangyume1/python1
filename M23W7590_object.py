# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:41:57 2023

@author: M23W7590楊楓 
"""
import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2+y**2)
p0 = Point(0,0)
p1 = Point(0,5)
p2 = Point(5,5)
p3 = Point(5,0)
print(p0.distance)
print(p1.distance)
print(p2.distance)
print(p3.distance)
    
