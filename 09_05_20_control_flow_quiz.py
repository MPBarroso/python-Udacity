# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:42:20 2020

@author: marco
"""

# '''
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 100
guess = 120

if guess <= answer*0.5:
    result = "Oops!  Your guess was too low."
elif guess >= answer*1.5:
    result = "Oops!  Your guess was too high."
elif answer == guess:
    result = "Nice!  Your guess matched the answer!"
else:
    result = "You are wrong"

print(result)