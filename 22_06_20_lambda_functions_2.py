# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:18:30 2020

@author: marco
"""
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

is_short = lambda x : len(x) < 10
#def is_short(name):
#    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)
