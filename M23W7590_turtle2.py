# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:14:34 2023

@author: M23W7590楊楓
"""
import turtle

t1 = turtle.Turtle()

t1.shape('turtle')
for i in range(3):
    t1.forward(100)
    t1.left(360/3)




t2 = turtle.Turtle()
t2.color('blue')
t2.shape('turtle')
t2.left(180)
t2.forward(50)

for i in range(36):    #130*36=5400，130度和360的最小公倍数
    t2.forward(100)
    t2.left(360/3 +10)  #1回130度旋转




turtle.done()



