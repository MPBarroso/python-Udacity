# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:06:22 2020

@author: marco
"""
# write your if statement here
points =52

if (points >= 1) and (points <= 50):
    prize=('wooden rabbit') 
    message = True

elif (points >= 151) and (points <= 180):
    prize=('wafer-thin mint')
    message = True
  
elif (points >= 181) and (points <= 200):
    prize=('penguin') 
    message = True
else:
    (points >= 51) and (points <= 150)
    prize=False
    message = False
    
if message is True:
    print('Congratulations! You won a {}!'.format(prize))
else:
    print('Oh dear, no prize this time.')
    
#'Congratulations! You won a [prize name]!'
 #'Oh dear, no prize this time.'