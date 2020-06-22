# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:41:25 2020

@author: marco
"""
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split()[0] for name in names]
# write your list comprehension here
print(first_names)

