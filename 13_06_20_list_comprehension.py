# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:30:47 2020

@author: marco
"""

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)