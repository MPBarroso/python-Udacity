# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:23:02 2020

@author: marco
"""
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points=dict(zip(labels, zip(x_coord, zip(y_coord,z_coord))))
for l,x in points.items():
    print(l,x)