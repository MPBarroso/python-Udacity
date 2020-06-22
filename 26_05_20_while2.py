# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:05:53 2020

@author: marco
"""
# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
# write your while loop here
#while current <= number:
#    product *= current
#    current += 1 
# multiply the product so far by the current number
# increment current with each iteration until it reaches number
# print the factorial of number
#print(product)

for n in range(1,number+1):
    product *= n
    #print(n)
#    print(product)
print(product)
    
    
#print(n)    
#print(product)
