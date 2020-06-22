# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:35:32 2020

@author: marco
"""
#a = [1, 5, 8]
#b = [2, 6, 9, 10]
#c = [100, 200]

#print(max([len(a), len(b), len(c)]))
#print(min([len(a), len(b), len(c)]))

#arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(arr[2:6])

#tuple_a = 1, 2
#tuple_b = (1, 2)

#print(tuple_a == tuple_b)
#print(tuple_a[0])

# Define a Dictionary, population,that provides information  on the world's largest cities.
# The key is the name of a city (a string), and the associated 
# value is its population in  millions of people.
#cities = {'Shanghai':17.8, 17.5:17, 'Istanbul':13.3,'Karachi':13.0,'Mumbai':12.5}
#print(cities.['Shangay'])
#cities['Shangay']
x = [1, 2, 3]
a = x
b = a
c = b 
#[1, 2, 3]


print(a == b)
print(a is b)
print(a == c)
print(a is c)
