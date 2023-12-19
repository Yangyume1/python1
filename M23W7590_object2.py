# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 01:52:44 2023

@author: M23W7590楊楓
"""
class AnimalZoo():
    def __init__(self, zoo_name="動物園の名前", zoo_number=0):
        self.name = zoo_name
        self.number = zoo_number
    def animal_up(self,zoo_number):
        self.number += zoo_number
    def zoo_info(self):
        print(f"{self.number}匹の動物が{self.name}にます")
my_zoo = AnimalZoo('kcg動物園')
my_zoo.animal_up(3)
my_zoo.zoo_info()
my_zoo.animal_up(4)
my_zoo.zoo_info()

        
        
        
        