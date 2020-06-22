# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:00:56 2020

@author: marco
"""
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

basket_fruits = dict.fromkeys(fruits , 0)
mix = basket_items.keys() & basket_fruits.keys()
basket_all = {k: basket_items[k] + basket_fruits[k] for k in mix}
fruit_count = sum(basket_all.values())
total_sum = sum(basket_items.values())
not_fruit_count = total_sum - fruit_count
#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count


print(fruit_count, not_fruit_count)