# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:43:50 2020

@author: marco
"""
scores = {"Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98}

passed = [key for key, value in scores.items() if value >= 65 ]

# write your list comprehension here
print(passed)
