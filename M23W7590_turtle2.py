# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:14:34 2023

@author: M23W7590楊楓
"""
import turtle
t1 = turtle.Turtle()
t1.color('red')
t1.shape('turtle')
for i in range(3):  #这是旋转的次数，三角形所以是三次
    t1.forward(100) #默认是右边，所以右边移动100
    t1.right(360/3)
#right是往右边移动120度，它原本是一条往右的直线，理解为顺时针方向旋转120度
t2 = turtle.Turtle()
t2.color('blue')
t2.shape('turtle')
t2.left(180)
t2.forward(50)
#乌龟原先是右方，所以首先调整方向，逆时针180
for i in range(36):    #130*36=5400，130度和360的最小公倍数
    t2.forward(100)
    t2.left(360/3 +10)  #1回130度旋转
turtle.done()




