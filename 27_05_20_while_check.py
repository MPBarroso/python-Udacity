# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:30:19 2020

@author: marco
"""
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_list = []
#while len(odd_list) <= 5:
for n in num_list:
    test_1 = n%2
    if test_1 == 1 and len(odd_list)<= 4:
        odd_list.append(n) 
        
print(odd_list)    
#print(len(odd_list))
#print(len(num_list))
