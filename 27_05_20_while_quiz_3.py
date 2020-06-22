# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:08:13 2020

@author: marco
"""
limit = 40


# write your while loop here
initial = 0
while initial**2 <= limit:
    initial += 1
#    print(initial)
#    nearest_square = initial**2
#    print(nearest_square)
nearest_square = (initial-1)**2
    

print(nearest_square)
