# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:43:42 2020

@author: marco
"""
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
#for key in cast:
#    print(key)
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))