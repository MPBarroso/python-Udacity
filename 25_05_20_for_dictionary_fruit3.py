# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:32:45 2020

@author: marco
"""
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for obj, count in basket_items.items():
   if obj in fruits:
       result += count
print(obj)
print("There are {} fruits in the basket.".format(result))