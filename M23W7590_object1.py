# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:20:40 2023

@author: M23W7590杨楓
"""
class Animals():
    def say(self): 
      print("私は動物です") 
      
class Tiger(Animals) :
    def say(self):
        print("私は虎です")
    def claim(self):
        print("私はラインです")
tiger = Tiger()
tiger.say()
tiger.claim()
animal = Tiger()
animal.say()
animal.claim()


    
