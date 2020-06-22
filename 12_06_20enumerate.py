# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:57:27 2020

@author: marco
"""
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
cast = list(zip(cast,heights))
for c in enumerate(cast):
    print(c)

#print(cast)
