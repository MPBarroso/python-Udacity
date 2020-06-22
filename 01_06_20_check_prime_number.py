# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:48:26 2020

@author: marco
"""
## Your code should check if each number in the list is a prime number
check_prime = [15,26, 39, 51, 53, 57, 79, 85]
number=2

#test = 1
#print(len(range(check_prime[0])))
#nb = " "
#cp= check_prime[0]%13

for i in check_prime:
    while i%number != 0:
           number+=1
    if number == i:
            print("{} IS a prime number".format(i))   
    elif number!=i:
            print("{} IS not a  prime number because {} is a factor of {}.".format(i,number,i))
    number=2         