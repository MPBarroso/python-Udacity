# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:48:44 2020

@author: marco
"""
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

basket_fruits = dict.fromkeys(fruits , 0)
#test_1 = set(dict.fromkeys(fruits , 0))
#test_3 = test_1.intersection(set(basket_items))

#result = sum(basket_items.values())

#res = dict.fromkeys(test_3, 0)

mix = basket_items.keys() & basket_fruits.keys()
basket_all = {k: basket_items[k] + basket_fruits[k] for k in mix}
result = sum(basket_all.values())
#for fruit, value in basket_items.items():
#    print("fruit: {}    quantitie: {}".format(fruit, value))


#    else:
#         test[fruit] += 1

#print(test_2)
print(mix)
print(result)

#    if fruit not in result:
#        result[fruit] = 1
#    else:
#        result[fruit] +=1 
#Rprint(result)