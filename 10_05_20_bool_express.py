# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:46:48 2020

@author: marco
"""

points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None    

# use the points value to assign prizes to the correct prize names


# use the truth value of prize to assign result to the correct prize


#print(result)

if points<=50:
    prize="wooden rabbit"
elif points<=150:
    prize=0
elif points<=180:
    prize="wafer-thin mint"
else:
    prize="penguin"
if prize:
    result="Congratulations! You won a {}!".format(prize)
else:
    result="Oh dear, no prize this time."
print (result)